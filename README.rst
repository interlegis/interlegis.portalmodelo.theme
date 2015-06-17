**************************
Temas para o Portal Modelo
**************************

.. contents:: Conteúdo
   :depth: 2


Introdução
==========

Este pacote provê vários temas com base no `Diazo <http://diazo.org>`_ para uso em sites `Plone <http://plone.org>`_ baseados no `Portal Modelo <http://www.interlegis.leg.br/portalmodelo>`_ do Interlegis.

O produto **interlegis.portlamodelo.theme** realiza as seguintes mudanças no Plone:

* Inclui o logo do interlegis no cabeçalho do site
* Inclui o título e a descrição do Plone Site no header
* Implementa uma nova formatação de resultado de busca
* Formata os portlets de navegação
* Traz os site_actions para o topo do site
* Oculta o colophon
* Adiciona os selos do Interlegis e da licença Creative Commons no rodapé
* Implementa o rodapé usando uma página site
* Implementa gatilhos responsivos para tablet e smartphones


Temas Disponíveis
=================

Tema Areia
----------

.. image:: https://raw.githubusercontent.com/interlegis/interlegis.portalmodelo.theme/master/src/interlegis/portalmodelo/theme/themes/Areia/preview.png
        :width: 200px
        :height: 110px

Tema Azul
---------

.. image:: https://raw.githubusercontent.com/interlegis/interlegis.portalmodelo.theme/master/src/interlegis/portalmodelo/theme/themes/Azul/preview.png
        :width: 200px
        :height: 110px

Tema Clean
----------

.. image:: https://raw.githubusercontent.com/interlegis/interlegis.portalmodelo.theme/master/src/interlegis/portalmodelo/theme/themes/Clean/preview.png
        :width: 200px
        :height: 110px

Tema Concreto
-------------

.. image:: https://raw.githubusercontent.com/interlegis/interlegis.portalmodelo.theme/master/src/interlegis/portalmodelo/theme/themes/Concreto/preview.png
        :width: 200px
        :height: 110px

Tema Gelo
---------

.. image:: https://raw.githubusercontent.com/interlegis/interlegis.portalmodelo.theme/master/src/interlegis/portalmodelo/theme/themes/Gelo/preview.png
        :width: 200px
        :height: 110px

Tema Kiwi
---------

.. image:: https://raw.githubusercontent.com/interlegis/interlegis.portalmodelo.theme/master/src/interlegis/portalmodelo/theme/themes/Kiwi/preview.png
        :width: 200px
        :height: 110px

Tema Moderno
------------

.. image:: https://raw.githubusercontent.com/interlegis/interlegis.portalmodelo.theme/master/src/interlegis/portalmodelo/theme/themes/Moderno/preview.png
        :width: 200px
        :height: 110px

Tema Vermelho
-------------

.. image:: https://raw.githubusercontent.com/interlegis/interlegis.portalmodelo.theme/master/src/interlegis/portalmodelo/theme/themes/Vermelho/preview.png
        :width: 200px
        :height: 110px

Tema IDG Amarelo
----------------

.. image:: https://raw.githubusercontent.com/interlegis/interlegis.portalmodelo.theme/master/src/interlegis/portalmodelo/theme/themes/IDG-amarelo/preview.png
        :width: 200px
        :height: 110px

Tema IDG Azul
-------------

.. image:: https://raw.githubusercontent.com/interlegis/interlegis.portalmodelo.theme/master/src/interlegis/portalmodelo/theme/themes/IDG-azul/preview.png
        :width: 200px
        :height: 110px

Tema IDG Branco
---------------

.. image:: https://raw.githubusercontent.com/interlegis/interlegis.portalmodelo.theme/master/src/interlegis/portalmodelo/theme/themes/IDG-branco/preview.png
        :width: 200px
        :height: 110px

Tema IDG Verde
--------------

.. image:: https://raw.githubusercontent.com/interlegis/interlegis.portalmodelo.theme/master/src/interlegis/portalmodelo/theme/themes/IDG-verde/preview.png
        :width: 200px
        :height: 110px

Tema Original
------------------

.. image:: https://raw.githubusercontent.com/interlegis/interlegis.portalmodelo.theme/master/src/interlegis/portalmodelo/theme/themes/Original/preview.png
        :width: 200px
        :height: 110px


Estado Deste Pacote
===================

O **interlegis.portalmodelo.theme** conta com testes automatizados e, a cada alteração em seu código, os testes são executados pelo serviço `Travis <https://travis-ci.org/>`_.

O estado atual dos testes, a cobertura de código e o número de downloads deste pacote podem ser vistos nas imagens a seguir:

.. image:: https://secure.travis-ci.org/interlegis/interlegis.portalmodelo.theme.png?branch=master
    :alt: Travis CI badge
    :target: http://travis-ci.org/interlegis/interlegis.portalmodelo.theme

.. image:: https://coveralls.io/repos/interlegis/interlegis.portalmodelo.theme/badge.png?branch=master
    :alt: Coveralls badge
    :target: https://coveralls.io/r/interlegis/interlegis.portalmodelo.theme

.. image:: https://pypip.in/d/interlegis.portalmodelo.theme/badge.png
    :target: https://pypi.python.org/pypi/interlegis.portalmodelo.theme/
    :alt: Downloads


Instalação
==========

Para habilitar a instalação deste produto em um ambiente que utilize o buildout:

1. Editar o arquivo buildout.cfg (ou outro arquivo de configuração utilizado) e adicionar o pacote ``interlegis.portalmodelo.theme`` à lista de eggs da instalação::

        [buildout]
        ...
        eggs =
            interlegis.portalmodelo.theme

2. Após alterar o arquivo de configuração é necessário executar ``bin/buildout``, que atualizará a sua instalação.

3. Reiniciar o Plone

4. Acesse o painel de controle e na opção **Temas** você verá os temas providos por este pacote listados.
