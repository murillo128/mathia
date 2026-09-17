# Remote two-jet repair trades KV distance for sign-phase complexity

A KV bound on the cumulative Chebyshev discrepancy does not control the absolute tail variation when signs can oscillate arbitrarily. It does control it once the number of sign-constant phases is counted.

For a tail beginning at `Y` with `M` sign phases,

`sum |c_q| log(q)/q <<_b (M + ell_KV(Y)) exp(-b V(Y))`.

The integrated `ell_KV` allowance is paid only once; each additional sign phase contributes one new endpoint/reset allowance of size `exp(-bV(Y))`. This is why alternations buy capacity only linearly rather than recreating a full KV tail each time.

With exact Mertens and first-boundary-slope matching, centering the slope at the barycenter of the first positive compensating phase leaves a residual tail debt of order `d_p ~ 1/(sqrt(p) log p)`, independently of the later sign pattern. Therefore

`sqrt(p) log(p) (M + ell_KV(Y)) exp(-bV(Y)) >> 1`.

Consequences: subpolynomial `M` cannot shift the leading `bV(Y)=(1/2)log p` horizon; delaying the repair to `(1/2+delta)log p` requires `M >= p^(delta-o(1))` sign phases. The surviving matched-control escape is thus high sign complexity, not merely one additional alternation.

This remains a conditional source-fidelity statement: the first Euler slope is extra information, not something yet derived from the Robin selector.