Para facilitar a criacao das tabelas que estamos a usar na traducao do `English as she is spoke`,
em https://wikisource.org/wiki/Index:O_Novo_Guia_da_Conversa%C3%A7%C3%A3o,_em_Portuguez_e_Inglez,_em_duas_partes.djvu,
fizemos este script para nao perdermos tempo com a formatacao.

Cada ficheiro representa uma tabela, organizado por colunas (ver pages/22b para um exemplo).
Os cabecalhos devem ser prefixados de um cardinal. Deve haver uma linha vazia entre cada bloco/coluna.

Exemplo:

  #Moveis d'uma casa
  O armario
  O bufete
  O escritorio

  #House hold goods
  The clothes-press
  The set of plate
  The bureau

  #Hau-ce hold gud'-ze
  Thi klothes-press
  Thi set ov plete
  Thi biuro

Se uma pagina a traduzir contiver mais do que uma tabela, criar um ficheiro por tabela.

Como correr: `./mw.py <nome-do-ficheiro>`
Correr o script gera um ficheiro `<nome-do-ficheiro>.mw` com a tabela em formato mediawiki.

Precisa de python3 instalado.
