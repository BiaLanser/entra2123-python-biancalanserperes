import datetime

def cal_dias(data):
    delta = datetime.now() - data
    return delta.days

dados_produtos = {
 1: {
     "nome": "Sabonete", 
     "id_for": 101, 
     "id_cat": 201, 
     "id_est":301,
     "id_loc": 401,
     "validade": datetime(2023, 5, 6),
     "dias_vencido":cal_dias(2023, 5, 6)
     },

 2: {
     "nome": "Arroz", 
     "id_for": 102, 
     "id_cat": 202, 
     "id_est":302,
     "id_loc": 402,
     "validade": datetime(2023, 1, 24),
     "dias_vencido":cal_dias(2023, 1, 24)
     },

 3: {
     "nome": "Smart TV", 
     "id_for": 103, 
     "id_cat": 203, 
     "id_est":303,
     "id_loc": 403,
     "validade": datetime(2020, 10, 20),
     "dias_vencido":cal_dias(2020, 10, 20)
     },

 4: {
     "nome": "Detergente", 
     "id_for": 104, 
     "id_cat": 204, 
     "id_est":304,
     "id_loc": 404,
     "validade": datetime(2023, 12, 22),
     "dias_vencido":cal_dias(2023, 12, 22)
     },

 5: {
     "nome": "Camiseta", 
     "id_for": 105, 
     "id_cat": 205, 
     "id_est":305,
     "id_loc": 405,
     "validade": datetime(2023, 6, 8),
     "dias_vencido":cal_dias(2023, 6, 8)
     },

 6: {
     "nome": "Shampoo", 
     "id_for": 101, 
     "id_cat": 201, 
     "id_est":306,
     "id_loc": 401,
     "validade": datetime(2023, 7, 2),
     "dias_vencido":cal_dias(2023, 7, 2)
     },

 7: {
     "nome": "Feijão", 
     "id_for": 102, 
     "id_cat": 202, 
     "id_est":307,
     "id_loc": 402,
     "validade": datetime(2023, 11, 2),
     "dias_vencido":cal_dias(2023, 11, 2)
     },

 8: {
     "nome": "Fone de Ouvido", 
     "id_for": 103, 
     "id_cat": 203, 
     "id_est":308,
     "id_loc": 403,
     "validade": datetime(2022, 10, 3),
     "dias_vencido":cal_dias(2022, 10, 3)
     },

 9: {
     "nome": "Água Sanitária", 
     "id_for": 104, 
     "id_cat": 204, 
     "id_est":309,
     "id_loc": 404,
     "validade": datetime(2023, 10, 19),
     "dias_vencido":cal_dias(2023, 10, 19)
     },

 10: {
     "nome": "Calça Jeans", 
     "id_for": 105, 
     "id_cat": 205, 
     "id_est":310,
     "id_loc": 401,
     "validade": datetime(2023, 10, 4),
     "dias_vencido":cal_dias(2023, 10, 2)
     },
}

dados_localizacao = {
    401: "Prateleira A",
    402: "Prateleira B",
    403: "Prateleira C",
    404: "Prateleira D",
    405: "Prateleira E",
}

dados_fornecedores = {
 101: "Super Distribuidora Alfa",
 102: "Mega Suprimentos Beta",
 103: "Excelente Electronics",
 104: "Produtos Limpos Delta",
 105: "ModaPlus Epsilon"
}


dados_categorias = {
 201: "Higiene Pessoal",
 202: "Alimentos",
 203: "Eletrônicos",
 204: "Limpeza",
 205: "Vestuário"
}

dados_estoque = {
 301: "10",
 302: "15",
 303: "20",
 304: "25",
 305: "30",
 306: "35",
 307: "40",
 308: "45",
 309: "50",
 310: "55",
}