# M2Agro Api

- [Produtos](#produtos)
- [Safras](#safras)
- [Serviços](#servicos)
- [Serviços x Produtos] (#servicos-produtos)

## Produtos

### Create

#### POST /produtos

BODY:

```javascript
{
    "nome": "Diesel",
    "preco": 30
}
```

#### GET /produtos/:id

BODY:

```javascript
{
    "id": 1,
    "nome": "Diesel",
    "preco": "30"
}
```


## Safras

### Create

#### POST /safras

BODY:

```javascript
{
    "nome": "Soja 2017",
    "data_inicial": "2017-01-01",
    "data_final": "2017-03-30",
}
```

#### GET /safras/:id

BODY:

```javascript
{
    "id": 1,
    "nome": "Soja 2017",
    "data_inicial": "2017-01-01",
    "data_final": "2017-03-30",
}
```

#### GET /safras/:id:/atualizar_servicos/
Atualiza os valores dos serviços da safra de acordo com os produtos utilizados por ele.
Outra alternativa é ir no django admin e selecionar a(s) safra(s) e selecionar a opção de atualizar os valores.


## Serviços

### Create

#### POST /servicos

BODY:

```javascript
{
    "nome": "Plantio",
    "data_inicial": "2017-01-02",
    "data_final": "2017-01-10",
    "safra": 1,
    "custo_total": "0.0" // será calculado posteriormente através da ação de atualizar os valores dos serviços
}
```
