# installs apache2

apache2:
  service:
    - running
    - name: apache2
    - enable: true    
    - reload: true
    - require:
      - pkg: apache2
    - watch:
      - pkg: apache2
  pkg:
    - installed
    - name: apache2