; Lab 14: Final Review

(define (compose-all funcs)
  (define (composed arg)
    (define (helper arg funcs)
      (cond ((null? funcs) arg)
            ((helper ((car funcs) arg) (cdr funcs)))))
    (helper arg funcs)
  )
  composed
)


;(define (compose-all funcs)
  ; (lambda (x)
  ;   (if (null? funcs) x)
  ;     ((compose-all (cdr (funcs))((car funcs) x)))))

(define (has-cycle? s)
  (define (pair-tracker seen_so_far curr)
    (cond ((null? curr) #f)
          ((contains? seen_so_far curr) #t)
          (else (pair-tracker (cons curr seen_so_far) (cdr-stream curr))))
    )
  (pair-tracker nil s)
)
;eq? checks if both list are pointing to the same list

(define (contains? lst s)
  (cond ((null? lst) #f)
        ((eq? (car lst) s) #t)
        (else (contains? (cdr lst) s))
  )
)
