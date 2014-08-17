pip:
  pkg:
    - installed
    - name: python-pip

build-essential:
  pkg:
    - installed
    - name: build-essential

texlive-full:
  pkg:
    - installed
    - name: texlive-full

sphinx:
  pip.installed:
    - name: sphinx
    - require:
      - pkg: python-pip

sphinxcontribphpdomain:
  pip.installed:
    - name: sphinxcontrib-phpdomain
    - require:
      - pkg: python-pip

pygments:
  pip.installed:
    - name: pygments
    - require:
      - pkg: python-pip

nose:
  pip.installed:
    - name: nose
    - require:
      - pkg: python-pip

coverage:
  pip.installed:
    - name: coverage
    - require:
      - pkg: python-pip
