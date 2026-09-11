# MI-002 — Ordinary divisor-sum arithmetic rejects composite substitute atoms at every fixed CA layer

**Evidence level:** supported by the exact block-factorization and sharp half-power event-scale separation in RE-058; this is a source-category boundary, not an RH consequence.

The generalized all-layer controls can assign a prime-form event tower to arbitrary PNT-dense integer labels, but ordinary `sigma(n)/n` does not respect that abstraction on composite labels. The mismatch is not confined to the first transition.

For a block label `q`, define the actual ordinary-divisor-sum layer increment

\[
\Lambda_j^\sigma(q)=\log\frac{\sigma(q^j)/q^j}{\sigma(q^{j-1})/q^{j-1}}.
\]

If `q=p` is prime, this equals the genuine CA increment

\[
\lambda_j(p)=\log\left(1+\frac1{p+p^2+\cdots+p^j}\right).
\]

For every composite `q` and fixed `j>=1`, internal prime factorization forces

\[
\Lambda_j^\sigma(q)\ge \frac14q^{-j+1/2},
\]

whereas the formal prime-label law is `lambda_j(q)=q^{-j}(1+O_j(q^{-1}))`. Thus the actual composite gain is larger by at least a factor of order `sqrt(q)`.

After transport through the CA tangent map `g(x)=1/(x log x)`, the formal prime-label event lies at scale `q^j`, while the true composite block event satisfies

\[
\zeta_{\sigma,j}(q)<8q^{j-1/2}.
\]

Prime squares make the exponent sharp:

\[
\zeta_{\sigma,j}(p^2)
=\left(\frac{2}{2j-1}+o_j(1)\right)q^{j-1/2}.
\]

So a composite integer cannot be treated as one prime-like atom while preserving the ordinary divisor-sum response through any fixed CA depth. Pairwise coprimality between labels does not repair the model because the obstruction lives **inside each composite label**: raising the block exponent activates all of its genuine prime coordinates simultaneously.

This changes what counts as a matched control. PNT density, common-source synchronization, and integrality can be faked, but once the ordinary `sigma` response is required, composite substitute atoms collapse back to the genuine-prime source category. The remaining flexibility is therefore in the global arrangement/coupling of actual prime coordinates, not in replacing primes by arbitrary integral generators with a synthetic tower.

**Boundary.** The estimate is fixed-layer and does not control `j` growing with `q`. It does not say that a quotient of consecutive genuine CA integers is prime, since several authentic prime-coordinate transitions can occur together. It also does not provide a distribution theorem for the surviving genuine primes or rule out an RH counterexample.
