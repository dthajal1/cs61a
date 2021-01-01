; ;;;;;;;;;;;;;;
; ; Questions ;;
; ;;;;;;;;;;;;;;
; Scheme
(define (cddr s) (cdr (cdr s)))

(define (cadr s) 'YOUR-CODE-HERE (car (cdr s)))

(define (caddr s)
  'YOUR-CODE-HERE
  (car (cdr (cdr s))))

(define (sign x)
  'YOUR-CODE-HERE
  (cond 
    ((= x 0) 0)
    ((< x 1) -1)
    (else    1)))

(define (square x) (* x x))

(define (pow b n)
  'YOUR-CODE-HERE
  (cond 
    ((zero? n) 1)
    ((even? n) (square (pow b (/ n 2))))
    (else      (* b (square (pow b (/ (- n 1) 2)))))))

(define (unique s)
  'YOUR-CODE-HERE
  (cond 
    ((null? s)
     ())
    (else
     (cons (car s)
           (unique
            (filter (lambda (x) (not (eq? (car s) x))) (cdr s))
            )))))
