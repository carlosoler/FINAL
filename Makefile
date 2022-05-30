enunciados:
	git web--browse www/index.html

all:
	@echo "Compilacion / ejecucion de la prueba"

clean:
	@echo "Limpiando..."

cliente:
	python3 cliente.py

servidor:
	python3 servidor.py

total_infinito:
    while true; do echo 'TOTAL' | make cliente ; done

frase_infinito:
    while true; do echo 'FRASE' | make cliente ; done
