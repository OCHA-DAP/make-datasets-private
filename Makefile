VENV=venv/bin/activate

run: $(VENV) force
	. $(VENV) && python3 make-datasets-private.py

$(VENV): requirements.txt
	rm -rf venv
	python3 -m venv venv
	. $(VENV) && pip3 install -r requirements.txt

force:

clean:
	rm -rf venv

