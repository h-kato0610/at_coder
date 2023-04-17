(defun is_even_or_odd(a b)
    (if (evenp (* a b))
        (format t "Even~%")
        (format t "Odd~%")))

(defun main()
    (let ((a (read))
          (b (read)))
            (is_even_or_odd a b)))

(main)