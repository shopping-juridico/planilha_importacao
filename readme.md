# Projeto de automatização de planilha de importação

> O trabalho consiste em integrar as ferramentas de programação da linguagem Python com o Microsoft Excel aplicada ao fluxo de importação de planilha do CP-PRO no Legal One, para otimizar o serviço.

----------------
## 1. O que é feito hoje

A partir do CP-PRO, é exportada uma planilha com dados do banco do escritório que são usados para preencher uma planilha a ser importada no Legal One.

## Descrição geral do fluxo

**1.1** CP-PRO -> Dados exportados

**1.2** Legal One -> Obtida a planilha de importação

**1.3** Planilha de importação preenchida com dados exportados do CP-Pro
* Manualmente, copiando e colando as informações nas respectivas colunas

**1.4** Ajustes e formatação dos dados
* Para que a importação ocorra sem erros e o sistema reconheça as informações, são necessários ajustes de formatação que muitas vezes envolve corrigir erros de inserção de dados.

----------------	
## 2. Problemas a serem avaliados

**2.1 PF/PJ**
* Células vazias -> precisa definir Pessoa Física ou Pessoa Jurídica
* Como é feito: Filtro no campo CPF/CNPJ: 'vazio' -> filtro no nome por parâmetros que identifiquem como CNPJ (s/a, bancos, cond)
	
**2.2 Validação CPF**	
* O sistema não reconhece se o CPF for inválido;
* O que deve ser feito:
  - Validar toda a coluna
  - Se for valido: Ok
  - Se for inválido: deixar em branco e identificar pf/pj a partir de "1"
  - Se for inválido: substituir pela forma válida -> automaticamente o sistema identifica PF ou PJ
	
**2.3 Depara de órgão**	
* Reconhecer o número e incluir o órgão correspondente;

**2.4 Padrão de capitalização de nomes**
* Incluir primeira letra maiúscula / preposições em minúsculo;
	
**2.5 Campos tabelados**
* Informações têm que ser idênticas às do L1 (acentos, caixa alta)

**2.6 Região**
* UF correspondente Cidade
* Utilizar a tabela do L1 como base

----------------	
## 3. Planejando

O algoritmo foi desenvolvido em sistema Linux, Ubuntu 20.04 versão LTS.

### 3.1 Preparando o ambiente

- Instalação do Python 3

```
sudo apt install python3
```

OBS: Nem sempre esse comando é necessário, pois na maioria das distribuições linux, Python já vem instalado.

- Instalação do venv (ambiente de desenvolvimento)
```
sudo apt update
sudo apt install python3 python3-dev python3-venv
```

- Instalação do pip (para instalar e gerenciar pacotes de bibliotecas python)

```
sudo apt update
sudo apt install pip3
```
- Editor de texto VS Code

   * Download do pacote .deb feito a partir do site oficial: https://code.visualstudio.com/
   * As extensões a serem usadas são referentes aos pacotes instalados, como o Openpyxl.

- Configurando o venv para isolar dependências

```
mkdir planilha importacao
cd planilha\ importacao
python3 -m venv env
```
OBS: a utilização de um ambiente de desenvolvimento, além de organizar melhor o projeto, isola as dependências e bibliotecas para que não haja interf>

- Ativando o ambiente

Fora do diretório do projeto, ou seja, em /home/projetos

```
source planilha\ importacao/bin/activate
```

depois, para eventualmente compilar o arquivo:

```
cd planilha\ importacao
```

### 3.2 Bibliotecas

- Instalação da biblioteca de manipulação de arquivos Excel:

```
pip3 install openpyxl
```

- Instalação da biblioteca pandas (para manipulação de dados em planilha):

```
pip3 install pandas
```
### 3.3 Desenvolvendo

- Exportação de dados do CP-PRO para arquivo .xlsx;
- Copiar arquivo .xlsx para a pasta do ambiente de desenvolvimento;
- Desenvolver algoritmo que:
    + Leia um arquivo .xlsx;
    + Valide CPF/CNPJ de colunas determinadas e indique de vermelho as células com informação inválida;
    + 
    + Salve um novo arquivo formatado.

----------------
## 4. Utilização

### 4.1 Método simples

> Compactar a pasta do projeto "planilha importacao" para o formato .zip e disponibilizar o arquivo para os outros usuários.

Desde que o usuário tenha Python instalado no sistema:

1. Descompactar a pasta;
2. Colar dentro dela os arquivos .xlsx com dados brutos;
3. Abrir o terminal dentro do diretório "planilha importacao" e executar o comando:
```
python3 planilha\ importacao.py
```

### 4.2 Método arquivo executável


### 4.3 Método interface gráfica

----------------
## 5. Resultados

----------------
## 6. Observações

Alguns pontos a serem otimizados demandam testes maiores e conforme determinada uma certa inviabilidade, a implementação pode ser descartada ou alterada.

