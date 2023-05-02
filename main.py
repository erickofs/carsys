import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QBoxLayout, QLabel, QPushButton, QWidget, QFileDialog, QCheckBox, QScrollArea, QDialog, QDialogButtonBox, QMessageBox, QLineEdit, QFormLayout, QComboBox, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QSizePolicy, QGridLayout, QGroupBox, QRadioButton, QButtonGroup, QDateEdit, QSpinBox, QDoubleSpinBox, QDateEdit, QTimeEdit, QPlainTextEdit, QScrollArea, QFrame, QGridLayout, QGroupBox, QRadioButton, QButtonGroup, QDateEdit, QSpinBox, QDoubleSpinBox, QDateEdit, QTimeEdit, QPlainTextEdit, QScrollArea, QFrame, QGridLayout, QGroupBox, QRadioButton, QButtonGroup, QDateEdit, QSpinBox, QDoubleSpinBox, QDateEdit, QTimeEdit, QPlainTextEdit, QScrollArea, QFrame, QGridLayout, QGroupBox, QRadioButton, QButtonGroup, QDateEdit, QSpinBox, QDoubleSpinBox, QDateEdit, QTimeEdit, QPlainTextEdit, QScrollArea, QFrame
from PySide6.QtCore import Qt, QDate, QTime
from car_dict import car_dict

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sistema de Cadastro de Carros')
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.cars = []
        self.initUI()
    
    def initUI(self):
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        register_button = QPushButton('Cadastrar Carros')
        search_button = QPushButton('Buscar Carros')
        view_button = QPushButton('Últimos Cadastros')
        main_layout.addWidget(register_button)
        main_layout.addWidget(search_button)
        main_layout.addWidget(view_button)
        self.setCentralWidget(main_widget)
        register_button.clicked.connect(self.register_car)
        search_button.clicked.connect(self.search_car)
        view_button.clicked.connect(self.view_last_register)

    def register_car(self):
        register_main_widget = QWidget()
        register_main_layout = QVBoxLayout()
        register_main_widget.setLayout(register_main_layout)
        register_form = QFormLayout()
        register_main_layout.addLayout(register_form)
        self.setCentralWidget(register_main_widget)
        
        # ID do carro. Será gerado automaticamente com base no número de carros cadastrados. Se não houver nenhum carro cadastrado, o ID será 1
        car_id_label = QLabel('ID')
        car_id_label.setAlignment(Qt.AlignCenter)
        car_id = QLineEdit()
        car_id.setReadOnly(True)
        car_id.setText(str(len(self.cars) + 1))
        # Add o label e o line edit no form layout
        register_form.addRow(car_id_label, car_id)
        
        # Marca do carro
        car_brand_label = QLabel('Marca')
        car_brand_label.setAlignment(Qt.AlignCenter)
        car_brand = QComboBox()
        car_brand.setEditable(True)
        car_brand.addItems(car_dict.keys())
        # Add o label e o combo box no form layout
        register_form.addRow(car_brand_label, car_brand)
        
        # Modelo do carro
        car_model_label = QLabel('Modelo')
        car_model_label.setAlignment(Qt.AlignCenter)
        car_model = QComboBox()
        car_model.setEditable(True)
        car_model.addItems(car_dict[car_brand.currentText()])
        # Atualize o modelo do carro de acordo com a marca selecionada
        def update_car_model():
            car_model.clear()
            car_model.addItems(car_dict[car_brand.currentText()])
        car_brand.currentTextChanged.connect(update_car_model)
        register_form.addRow(car_model_label, car_model)
        
        # Ano do carro
        car_year_label = QLabel('Ano')
        car_year_label.setAlignment(Qt.AlignCenter)
        car_year = QComboBox()
        car_year.setEditable(True)
        # Adiciona os anos de 1950 até o ano atual
        for year in range(1950, QDate.currentDate().year() + 1):
            car_year.addItem(str(year))
        # Add o label e o combo box no form layout
        register_form.addRow(car_year_label, car_year)
            
        # Cadastre o carro na tabela implementando a função check_empty_fields
        def register_car_process():
            if car_brand.currentText() == '' or car_model.currentText() == '' or car_year.currentText() == '':
                QMessageBox.warning(self, 'Erro', 'Preencha todos os campos')
            else:
                # Adicione o carro na lista de carros
                self.cars.append([car_id.text(), car_brand.currentText(), car_model.currentText(), car_year.currentText()])
                # Adicione o carro na tabela
                register_table.setRowCount(len(self.cars))
                register_table.setItem(len(self.cars) - 1, 0, QTableWidgetItem(car_id.text()))
                register_table.setItem(len(self.cars) - 1, 1, QTableWidgetItem(car_brand.currentText()))
                register_table.setItem(len(self.cars) - 1, 2, QTableWidgetItem(car_model.currentText()))
                register_table.setItem(len(self.cars) - 1, 3, QTableWidgetItem(car_year.currentText()))
                # Limpe os campos
                car_id.setText(str(len(self.cars) + 1))
                car_brand.setCurrentText('')
                car_model.setCurrentText('')
                car_year.setCurrentText('')
        
        # Botão para cadastrar o carro
        register_button = QPushButton('Cadastrar')
        register_button.clicked.connect(register_car_process)
        register_form.addRow(register_button)
        
        # Botão para voltar ao menu principal
        back_button = QPushButton('Voltar')
        back_button.clicked.connect(self.initUI)
        register_form.addRow(back_button)
        
        # Crie uma tabela para armazenar o ID, a marca, o modelo e o ano do carro
        register_table = QTableWidget()
        register_table.setColumnCount(4)
        register_table.setHorizontalHeaderLabels(['ID', 'Marca', 'Modelo', 'Ano'])
        register_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        register_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        register_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        register_table.setSortingEnabled(True)
        register_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        register_main_layout.addWidget(register_table)
    
    def search_car(self):
        search_main_widget = QWidget()
        search_main_layout = QVBoxLayout()
        search_main_widget.setLayout(search_main_layout)
        search_form = QFormLayout()
        search_main_layout.addLayout(search_form)
        self.setCentralWidget(search_main_widget)
        
        # Crie um combo box para selecionar o campo de busca
        search_field_label = QLabel('Campo de Busca')
        search_field_label.setAlignment(Qt.AlignCenter)
        search_field = QComboBox()
        search_field.addItems(['ID', 'Marca', 'Modelo', 'Ano'])
        
        # Crie uma função para adicionar outro campo de busca
        def add_search_field():
            # Crie um combo box para selecionar o campo de busca
            search_field_label = QLabel('Campo de Busca')
            search_field_label.setAlignment(Qt.AlignCenter)
            search_field = QComboBox()
            search_field.addItems(['ID', 'Marca', 'Modelo', 'Ano'])
            # Adicione o label e o combo box no layout
            search_main_layout.addWidget(search_field_label)
            search_main_layout.addWidget(search_field)
            # Crie um line edit para inserir o valor de busca
            search_value_label = QLabel('Valor de Busca')
            search_value_label.setAlignment(Qt.AlignCenter)
            search_main_layout.addWidget(search_value_label)
        
        search_value = QLineEdit()
        # Adicione o label e o line edit no form layout
        search_form.addRow(search_value)

        # Adicione a tabela de resultados
        search_table = QTableWidget()
        search_table.setColumnCount(4)
        search_table.setHorizontalHeaderLabels(['ID', 'Marca', 'Modelo', 'Ano'])
        search_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        search_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        search_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        search_table.setSortingEnabled(True)
        search_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        search_main_layout.addWidget(search_table)

        # Crie uma função para realizar a busca na tabela de registros e adicionar os resultados na tabela de resultados
        def search_car_process():
            # Limpe a tabela de resultados
            search_table.setRowCount(0)
            # Verifique se o campo de busca e o valor de busca estão vazios
            if search_field.currentText() == '' or search_value.text() == '':
                QMessageBox.warning(self, 'Erro', 'Preencha todos os campos')
            else:
                # Verifique se o campo de busca é o ID
                if search_field.currentText() == 'ID':
                    # Verifique se o ID é um número
                    if search_value.text().isdigit():
                        # Verifique se o ID existe
                        if int(search_value.text()) <= len(self.cars):
                            # Adicione o carro na tabela de resultados
                            search_table.setRowCount(1)
                            search_table.setItem(0, 0, QTableWidgetItem(self.cars[int(search_value.text()) - 1][0]))
                            search_table.setItem(0, 1, QTableWidgetItem(self.cars[int(search_value.text()) - 1][1]))
                            search_table.setItem(0, 2, QTableWidgetItem(self.cars[int(search_value.text()) - 1][2]))
                            search_table.setItem(0, 3, QTableWidgetItem(self.cars[int(search_value.text()) - 1][3]))
                        else:
                            QMessageBox.warning(self, 'Erro', 'ID não encontrado')
                    else:
                        QMessageBox.warning(self, 'Erro', 'ID inválido')
                # Verifique se o campo de busca é a marca
                elif search_field.currentText() == 'Marca':
                    # Verifique se a marca existe
                    if search_value.text() in car_dict.keys():
                        # Adicione os carros da marca na tabela de resultados
                        search_table.setRowCount(len(car_dict[search_value.text()]))
                        for row in range(len(car_dict[search_value.text()])):
                            search_table.setItem(row, 0, QTableWidgetItem(self.cars[row][0]))
                            search_table.setItem(row, 1, QTableWidgetItem(self.cars[row][1]))
                            search_table.setItem(row, 2, QTableWidgetItem(self.cars[row][2]))
                            search_table.setItem(row, 3, QTableWidgetItem(self.cars[row][3]))
                    else:
                        QMessageBox.warning(self, 'Erro', 'Marca não encontrada')
                # Verifique se o campo de busca é o modelo
                elif search_field.currentText() == 'Modelo':
                    # Verifique se o modelo existe
                    if search_value.text() in car_dict.values():
                        # Adicione os carros do modelo na tabela de resultados
                        search_table.setRowCount(len(car_dict[search_value.text()]))
                        for row in range(len(car_dict[search_value.text()])):
                            search_table.setItem(row, 0, QTableWidgetItem(self.cars[row][0]))
                            search_table.setItem(row ,1, QTableWidgetItem(self.cars[row][1]))
                            search_table.setItem(row, 2, QTableWidgetItem(self.cars[row][2]))
                            search_table.setItem(row, 3, QTableWidgetItem(self.cars[row][3]))
                    else:
                        QMessageBox.warning(self, 'Erro', 'Modelo não encontrado')
                # Verifique se o campo de busca é o ano
                elif search_field.currentText() == 'Ano':
                    # Verifique se o ano é um número
                    if search_value.text().isdigit():
                        # Verifique se o ano existe
                        if search_value.text() in car_dict.values():
                            # Adicione os carros do ano na tabela de resultados
                            search_table.setRowCount(len(car_dict[search_value.text()]))
                            for row in range(len(car_dict[search_value.text()])):
                                search_table.setItem(row, 0, QTableWidgetItem(self.cars[row][0]))
                                search_table.setItem(row, 1, QTableWidgetItem(self.cars[row][1]))
                                search_table.setItem(row, 2, QTableWidgetItem(self.cars[row][2]))
                                search_table.setItem(row, 3, QTableWidgetItem(self.cars[row][3]))
                        else:
                            QMessageBox.warning(self, 'Erro', 'Ano não encontrado')
                    else:
                        QMessageBox.warning(self, 'Erro', 'Ano inválido')
    
        # Crie um botão para realizar a busca
        search_button = QPushButton('Buscar')
        search_button.clicked.connect(search_car_process)
        search_main_layout.addWidget(search_button)
        
    
    def view_last_register(self):
        pass

if __name__ == '__main__':
    app = QApplication([])
    app.setStyle('Fusion')
    janela = MainWindow()
    janela.show()
    app.exec()

