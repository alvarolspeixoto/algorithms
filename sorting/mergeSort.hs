mergeSort :: [Int] -> [Int]
mergeSort [] = []
mergeSort [x] = [x]
mergeSort xs = intercala (mergeSort vs) (mergeSort us)
    where
      meio = div (length xs) 2
      us   = take meio xs
      vs   = drop meio xs

intercala :: [Int] -> [Int] -> [Int]
intercala xs [] = xs
intercala [] ys = ys
intercala (x:xs) (y:ys)
    | x <= y    = x : intercala xs (y:ys)
    | otherwise = y : intercala (x:xs) ys