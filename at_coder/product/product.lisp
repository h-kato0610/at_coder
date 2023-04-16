(defun main()
    (let ((a (read))
          (b (read)))
        (let ((c (* a b)))
            (if (= (rem c 2) 0)
                (write-line "Even")
                (write-line "Odd")))))

(main)