def generate(answers, coords, clues) :

  across_answers = answers[0]
  down_answers = answers[1]

  across_clues = clues[0]
  down_clues = clues[1]

  across_count = len(across_answers)
  down_count = len(down_answers)

  print('<ACROSS PUZZLE>')
  print('<TITLE>')
  print('     Crossword')
  print('<AUTHOR>')
  print('     Across Lite *.txt file Generator')
  print('<COPYRIGHT>')
  print('     GPL')
  print('<SIZE>')
  print('     15x15')
  print('<GRID>')
  print('ASTROLABIO.ALUD')
  print('S.E.R.S.N.F.O.I')
  print('CINTA.COFRADIAS')
  print('E.I.D.O.A.U.N.C')
  print('TOSTON.AMANSADO')
  print('A.T.R.C.E.O.S.L')
  print('.TABACO..ASE..O')
  print('O.S...L.S...U.S')
  print('R..RAP..OSCURA.')
  print('F.P.D.C.R.H.D.S')
  print('EVAPORAR.CARIBE')
  print('B.R.R.M.L.R.M.M')
  print('RECONDITO.LIBIA')
  print('E.H.O.O.O.A.R.N')
  print('SOEZ.INTRINSECA')
  print('<ACROSS>')
  for i in xrange(across_count) :
    clue = across_clues[i][1]
    print("     %s" % (clue))
  print('<DOWN>')
  for i in xrange(down_count) :
    clue = down_clues[i][1]
    print("     %s" % (clue))
  print('<NOTEPAD>')
  print('Good luck')
