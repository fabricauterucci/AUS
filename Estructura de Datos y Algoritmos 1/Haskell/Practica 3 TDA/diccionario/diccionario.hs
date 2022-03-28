newtype Dict a = Dicc (Bintree a) deriving Show

mkDict = Dicc (mkNewTree)

insertDict x (Dicc t) = Dicc (addTree x t)

inDict x (Dicc t) = inTree x t

delDict x (Dicc t) = Dicc (delTree x t)