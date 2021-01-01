
; Tail recursion

(define (replicate x n)
  (define (replicate-helper x n result)
   (if (= n 0) result
     (replicate-helper x (- n 1) (cons x result))))
  (replicate-helper x n nil)
  )

(define (accumulate combiner start n term)
  (cond ((= n 0) start)
        (else (combiner (term n) (accumulate combiner start (- n 1) term)))
    )
)

(define (accumulate-tail combiner start n term)
(define (acc-helper n result)
  (cond ((= n 0) result )
      (else (acc-helper (- n 1) (combiner (term n) result))))
  )
(acc-helper n start)
)

; Streams

(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define multiples-of-three
  (cons-stream 3 (map-stream (lambda (x) (+ x 3)) multiples-of-three))
)

(define (make-decre-list s)
    (if (null? s) nil
    (if (null? (cdr-stream s)) (cons (car s) nil)
    (if (> (car s) (car (cdr-stream s))) (cons (car s) nil)
      (cons (car s) (make-decre-list (cdr-stream s)))))))


(define (next-decre-list s)
    (if (null? s) nil
    (if (null? (cdr-stream s)) nil
    (if (> (car s) (car (cdr-stream s))) (cdr-stream s)
      (next-decre-list (cdr-stream s))))))


(define (nondecreastream s)
    (if (null? s) nil
    (cons-stream (make-decre-list s) (nondecreastream (next-decre-list s))))
)


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))
