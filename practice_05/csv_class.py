import csv


class CSV_Manager:
    def __init__(self, csv_file, delim=';', code='cp1251'):
        self._csv_file = csv_file
        self._delimiter = delim
        self._code = code
        self._data = []
        self.reader = None

        self.import_file()

    @property
    def csv_file(self):
        return self._csv_file

    @csv_file.setter
    def csv_file(self, csv_file_val):
        self._csv_file = csv_file_val

    @property
    def delim(self):
        return self._delimiter

    @delim.setter
    def delim(self, delim_val):
        self._delimiter = delim_val

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code_val):
        self._code = code_val

    def import_file(self):
        with open(self._csv_file) as csv_f:
            self.reader = csv.reader(csv_f, delimiter=self._delimiter)
            self._data.clear()
            for i in self.reader:
                self._data.append(i)

    def export_file(self):
        with open(self._csv_file, 'w', encoding=self._code) as csv_f:
            writer = csv.writer(csv_f, delimiter=self._delimiter)
            writer.writerows(self._data)

    def len_column(self):
        """возвращает количество столбиков таблицы."""
        try:
            return len(self._data[0])
        except:
            return None

    def len_lines(self):
        """возвращает количество строк таблицы"""
        return len(self._data)

    def get_headers(self):
        """вернуть список заголовков колонок"""
        try:
            return self._data[0]
        except:
            return None

    def get_column(self, column):
        """принимает аргумент в виде номера или заголовка колонки,
            возвращает список записей в данножй колонке, начиная с заголовка колонки."""
        column_list = []

        data_index = None
        if isinstance(column, int):
            data_index = column - 1
        elif isinstance(column, str):
            data_index = self._data[0].index(column)

        for line in self._data:
            try:
                column_list.append(line[data_index])
            except:
                continue

        return column_list

    def get_line(self, numb_line):
        """принимает аргумент, в виде номера строки таблицы,
        возвращает список записей в указанной строке."""
        try:
            return self._data[numb_line - 1]
        except:
            return None

    def get_cells(self, *args):
        """принимает номер колонки и строки в виде списка из двух элементов,
        где первое значение - номер колонки, второе - номер строки.
        Может принимать *args подобных запросов и возвращать список значений, по указанным координатам."""
        cells_list = []

        for list_YX in args:
            for y, x in list_YX:
                try:
                    line_x = self._data[x - 1]
                    cell = line_x[y - 1]
                    cells_list.append(cell)
                except:
                    continue

        return cells_list

    def add_header(self, name_column, numb_column=None):
        """принимает аргумент в виде имени заголовка для новой колонки,
          вторым, необязательным, аргументом, принимает номер для новой колонки.
          По умолчанию, колонка создается в последней Т.Е. правой.
          Все значения для новой колонки, забиваются типом пустой строки ''.
          Учитываем, что '' - это пустое значение в csv файле Т.Е.
          ;; - между ними мы предполагаем ''."""

        len_c = self.len_column()
        first_line = self._data[0]
        if numb_column and isinstance(numb_column, int) and numb_column != len_c:

            first_line.insert(numb_column - 1, name_column)

            for line in self._data:
                if line == first_line:
                    continue
                line.insert(numb_column - 1, '')
        else:
            first_line.append(name_column)

            for line in self._data:
                if line == first_line:
                    continue
                line.append('')

    def set_cell(self, list_YX, value):
        """принимает аргумент, в виде списка из двух значений
          для колонки и строчки или в виде списка из двух значений,
          где первое значение - имя колонки, второе - номер строки;
          вторым аргументом принимает значение для ячейки и устанавливает его.
          Не разрешает изменять первую строку, где находятся заголовки."""

        try:
            y, x = list_YX[0], list_YX[1]
            line_x = self._data[x - 1]
            if not line_x == self._data[0]:
                line_x[y - 1] = value
            else:
                print('ERROR - first line blocked for changing')
        except:
            return None

    def add_line(self, new_line, numb_line=None):
        """принимает список значений для строки и номер строки,
          где нужно вставить новую строку.
          Если какую-то ячейку нужно пропустить, в списке будет стоять значение ''.
          По умолчанию добавляет строку в конец."""

        len_line_date = self.len_column()
        len_new_line = len(new_line)
        rasn = len_line_date - len_new_line

        if len_line_date > len_new_line:
            while rasn > 0:
                new_line.append('')
                rasn -= 1

        if numb_line and isinstance(numb_line, int) and numb_line > 0:
            self._data.insert(numb_line - 1, new_line)
        else:
            self._data.append(new_line)

    def save(self):
        """сохраняет текущее состояние в объект файла, с указанным разделителем и в указанной кодировке."""
        self.export_file()


def main():
    c_s_v = CSV_Manager('SalesPerson1.csv')
    print('len of colums - ', c_s_v.len_column())
    k = ([4, 2], [5, 3], [6, 2])
    print(c_s_v.get_cells(k))

    c_s_v.add_header('Компания', 1)
    print(c_s_v.get_headers())
    print(c_s_v.get_line(2))

    c_s_v.set_cell([1, 2], 'ELDORADO')
    print(c_s_v.get_line(2))

    new_line = [f'{i + 1}.Test' for i in range(15)]
    c_s_v.add_line(new_line, 2)
    print(c_s_v.get_line(1))
    print(c_s_v.get_line(2))
    print(c_s_v.get_line(3))

    c_s_v.save()


if __name__ == '__main__':
    main()
