(def numbers (map #(Integer/parseInt %) (re-seq #"\d+" (slurp "input.txt"))))
(println numbers)

(defn sumsto2020? 
    ([x y] (= 2020 (+ x y)))
    ([x y z] (= 2020 (+ x y z)))
)

(doseq [a numbers b numbers] (if (sumsto2020? a b)(println (* a b))))
(doseq [a numbers b numbers c numbers] (if (sumsto2020? a b c) (println (* a b c))))