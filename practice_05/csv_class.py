import csv


class CSV_Manager:
    def __init__(self, csv_file, delim=';', code='cp1251'):
        self._csv_file = csv_file
        self._delim = delim
        self._code = code
        self._data = []
        self.reader = None

    @property
    def csv_file(self):
        return self._csv_file

    @csv_file.setter
    def csv_file(self, csv_file_val):
        self._csv_file = csv_file_val

    @property
    def delim(self):
        return self._delim

    @delim.setter
    def delim(self, delim_val):
        self._delim = delim_val

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code_val):
        self._code = code_val

    def import_file(self):
        with open(self._csv_file) as csv_f:
            self.reader = csv.reader(csv_f, delimiter=self._delim)
            self._data.clear()
            for i in self.reader:
                self._data.append(i)

    def export_file(self):
        with open(self._csv_file, 'w') as csv_f:
            writer = csv.writer(self._csv_file, delimiter=self._delim)
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
        if isinstance(column, int):
            for line in self.reader:
                try:
                    column_list.append(line[column - 1])
                except:
                    continue
        elif isinstance(column, str):
            for line in self.reader:
                try:
                    column_list.append(line[column])
                except:
                    continue

        return column_list

    def get_line(self, no_line):
        """принимает аргумент, в виде номера строки таблицы,
        возвращает список записей в указанной строке."""
        try:
            return self._data[no_line - 1]
        except:
            return None

    def get_cells(self, *args):
        """принимает номер колонки и строки в виде списка из двух элементов,
        где первое значение - номер колонки, второе - номер строки.
        Может принимать *args подобных запросов и возвращать список значений, по указанным координатам."""
        cells_list = []
        
        for cords in args:
                       
            try:
                x,y  = cords[0], cords[1]             
                line_x = self._data[x-1]
                cell = line_x[y-1]                
                cells_list.append(value)            
 
            except:
                continue
                
        return cells_list    
        
        
         

    def add_header(self, name_column, no_column=None):
        """принимает аргумент в виде имени заголовка для новой колонки,
          вторым, необязательным, аргументом, принимает номер для новой колонки.
          По умолчанию, колонка создается в последней Т.Е. правой.
          Все значения для новой колонки, забиваются типом пустой строки ''.
          Учитываем, что '' - это пустое значение в csv файле Т.Е.
          ;; - между ними мы предполагаем ''."""
        
        len_c =  self.len_column()
        
        if no_column and isinstance(no_column,int) and no_column!=len_c:
            first_line = self._data[0]
            first_line.insert(no_column-1,name_column)
            
            for line in self._data:
                if line == first_line:
                    continue
                line.insert(no_column-1,'')
        else:
            first_line.append(name_column)
            
            for line in self._data:
                if line == first_line:
                    continue
                line.append('')
            
             
            
            
            

    def set_cell(self, list_xy, value):
        """принимает аргумент, в виде списка из двух значений
          для колонки и строчки или в виде списка из двух значений,
          где первое значение - имя колонки, второе - номер строки;
          вторым аргументом принимает значение для ячейки и устанавливает его.
          Не разрешает изменять первую строку, где находятся заголовки."""
        
        try:
             
            x,y  = cords[0], cords[1]             
            line_x = self._data[x-1]
            line_x[y-1] =  value 
            
 
        except:
            return None
            
         
        
         

    def add_line(self, list_line, no_line=None):
        """принимает список значений для строки и номер строки,
          где нужно вставить новую строку.
          Если какую-то ячейку нужно пропустить, в списке будет стоять значение ''.
          По умолчанию добавляет строку в конец."""
        pass

    def save(self):
        """сохраняет текущее состояние в объект файла, с указанным разделителем и в указанной кодировке."""
        pass
