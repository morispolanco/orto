import streamlit as st
from spellchecker import SpellChecker


spell = SpellChecker() # Instancia de la clase para corregir errores ortográficos. 


def main():     / * Función principal donde se ejecuta el programa completo* /  	    texto_original=st.text_area("Escribe aquí:")# Creación del widget "Text Area" en Streamlit, que permite escribir un párrafo entero y no solo palabras sueltas como con el widget anterior (input)      if(len(texto_original)!=0):          misspelled = spell.unknown([word for word in texto_original])           corrector={}            for i in range(len((misspelled))):              lista=(list)(spell.candidates(*[str((misspelled)[i])]))               opciones=[x+' 'for x in lista ]                             valores=[y+1 for y in range ((opciones).__sizeof__()) ]                tuplas2=(zip)(valores,opciones )                  corrector[str('palabra') + str('{}:'.format({i}) )]=' '.join([z+(',').strip()for z , w in tuplas2])                          st.write(corrector)           if (st.button("Corregir")):              for i in range((misspelled).__sizeof__() ):                  texto_original=texto_original .replace(*[str('{}'.format({i})), str(lista [0] ) ])                   #print (' '.join([x+' 'for x in lista ]))               print ("Texto corregido:",texto_original  )               
if __name__ == "main":     main ()
 
