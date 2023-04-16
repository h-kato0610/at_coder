(defun main()
        (let ((a (read))
              (b (read))
              (c (read))
              (s (read-line)))
    (format t "~A ~A~%" (+ a b c) s)))

(main)