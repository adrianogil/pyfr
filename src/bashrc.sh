if [ -z "$PYFR_PYTHON_PATH" ]
then
    export PYFR_PYTHON_PATH=$PYFR_SOURCE_DIR/python/
    export PYTHONPATH=$PYFR_PYTHON_PATH:$PYTHONPATH
fi

alias fr-conjugueur="python2 -m fr.conjugueur"
alias fr-gen-phrase="python2 -m fr.phrasesaleatoires"