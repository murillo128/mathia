# RE-255 — The critical triangular Robin moment is a sharp endpoint Chebyshev/count contrast

**Status:** EXACT-DERIVED + SHARP-SOURCE-FIDELITY-THRESHOLD + CLASSICAL-TAYLOR/ABEL-BRIDGE + ORDINARY-PRIME-APPLICATION-OPEN; independent adversarial review pending.

**Dependencies:** RE-021 (selected colossally abundant frontier and endpoint), RE-252 (Guth–Maynard error-balance horizon), RE-253 (ordinary-prime signed triangular moment and Robin local-kernel reduction), RE-254 (CA-prefix-frozen matched transport with critical moment separation).

RE-253 converts the unresolved first-annulus Robin contribution at the Guth–Maynard horizon into an integrated, signed error of the ordinary-prime counting function. RE-254 proves that its critical cancellation cannot be deduced merely from the CA-frozen initial prime source and the uniform short-interval counting envelope. The following exact identity identifies **which additional endpoint information** restores rigidity: a jointly centered count and Chebyshev increment. When the total number of atoms is matched, its necessary precision is exactly an \(o(\sqrt p/\log p)\) *difference of logarithmic prime-weight sums*. RE-254's matched pair shows this order cannot be relaxed to a big-O condition in that source class.

## 1. Exact endpoint identity

Let \(p\) be an ordinary prime, \(L=\log p\), and \(1\le H\le p/2\). Let \(Q\) be any locally finite increasing positive **real-label** source (ordinary primes are one case) with finitely many labels in \((p,p+H]\). Put
\[
\begin{aligned}
M_Q&=\#\{r\in Q:p<r\le p+H\},\\
\Theta_Q&=\sum_{\substack{r\in Q\\p<r\le p+H}}\log r,\\
D_{Q,p}(H)&=\sum_{\substack{r\in Q\\p<r\le p+H}}
        \bigl(H-(r-p)\bigr)-\frac{H^2}{2L},\\
\mathcal E_{Q,p}(H)&=
\Theta_Q-\left(L+\frac Hp\right)M_Q+\frac{H^2}{2pL}.
\end{aligned}\tag{1}
\]
The last quantity is a **joint endpoint contrast**; a count estimate for \(M_Q\) alone, or a Chebyshev estimate for \(\Theta_Q\) alone, is not automatically an estimate of this contrast.

Define the nonnegative logarithmic-concavity defect
\[
Z_{Q,p}(H)=
\sum_{\substack{r\in Q\\p<r\le p+H}}
\left[(r-p)-p\log\frac rp\right].
\tag{2}
\]
Then the following holds **exactly**, without prime-distribution assumptions:
\[
\boxed{\quad
D_{Q,p}(H)=-p\,\mathcal E_{Q,p}(H)-Z_{Q,p}(H),\qquad
0\le Z_{Q,p}(H)\le\frac{M_QH^2}{2p}.
\quad}\tag{3}
\]

**Proof.** Write \(y_r=r-p\). Since
\(\Theta_Q=L M_Q+\sum_r\log(1+y_r/p)\), multiplying the definition of
\(\mathcal E\) by \(-p\) gives
\[
-p\mathcal E
=HM_Q-p\sum_r\log(1+y_r/p)-\frac{H^2}{2L}.
\]
Subtracting \(Z=\sum_r(y_r-p\log(1+y_r/p))\) leaves
\(HM_Q-\sum_r y_r-H^2/(2L)=D\). The elementary inequalities
\(0\le u-\log(1+u)\le u^2/2\), for \(u\ge0\), give the stated bound. The prime or CA properties of \(Q\) are not used.

## 2. Critical-horizon fidelity and equivalence

Let the horizon be exactly the RE-252/RE-253 error-balance scale
\[
H=H_\star(p)=\frac{p^{3/4}}{\sqrt L}
                  \exp\left(\frac12 L^{1/4}\right).
\tag{4}
\]
Suppose a family of sources satisfies a common count bound
\(M_Q\le C H/L\), for a constant \(C\) independent of \(p\) and the source.
This follows, for example, for the ordinary primes and the RE-254 matched
sources from their uniform Guth–Maynard-scale estimate at the displayed
horizon. By (3),
\[
\left|
\frac L{p^{3/2}}D_{Q,p}(H)
+\frac L{\sqrt p}\mathcal E_{Q,p}(H)\right|
\le \frac{C H^3}{2p^{5/2}}
=\frac C2\,p^{-1/4}L^{-3/2}
                \exp\left(\frac32L^{1/4}\right)=o(1).
\tag{5}
\]
Consequently, for every such source family,
\[
\boxed{\quad
D_{Q,p}(H_\star)=o(p^{3/2}/L)
\quad\Longleftrightarrow\quad
\mathcal E_{Q,p}(H_\star)=o(\sqrt p/L).
\quad}\tag{6}
\]
The equivalence is along any selected sequence on which the displayed
bounds hold. It is **not** an unconditional statement that either
smallness condition is true for the ordinary primes.

For two source families with the **same shell cardinality**
\(M_+=M_-\le CH/L\), their count and deterministic centering terms cancel:
\[
\boxed{\quad
\frac L{p^{3/2}}(D_+-D_-)
=-\frac L{\sqrt p}(\Theta_+-\Theta_-)+o(1).
\quad}\tag{7}
\]
Hence
\[
D_+-D_-=o(p^{3/2}/L)
\quad\Longleftrightarrow\quad
\Theta_+-\Theta_-=o(\sqrt p/L).
\tag{8}
\]
If the two counts are not equal, the right-hand side of (7) must instead
contain their **joint contrast**
\(\Delta\Theta-(L+H/p)\Delta M\). It would be incorrect to use the
Chebyshev increment alone for unmatched sources.

For the **ordinary-prime** source at a RE-021-selected self-tangent CA
frontier, RE-253's local kernel expansion (equations (11) and (14) there)
and (5) also imply the equivalent first-annulus normal form
\[
\boxed{\quad
\sqrt p L\int_p^{p+H_\star} I(t)\,dt
=\frac L{\sqrt p}\,\mathcal E_{P,p}(H_\star)+o(1).
\quad}\tag{9}
\]
Here \(I\) is the *ordinary-prime* Robin kernel of RE-253, and the
\(o(1)\) includes that result's \(O(L^{-1}+p^{-1/5})\) error. Formula (9)
does not determine the sign or the value of the contrast.

## 3. Sharpness within the actual-prefix-frozen matched controls

Apply (7) to the two sources \(Q_p^+,Q_p^-\) constructed in RE-254. For
every fixed transport amplitude \(a>0\), their **complete source prefixes
through the genuine selected CA state are identical to the ordinary
primes**; they have the same number of atoms in the critical shell,
preserve ranks and exterior labels, and obey one uniform-in-sign
Guth–Maynard short-interval **error envelope**. RE-254 proves
\[
\frac L{p^{3/2}}
\bigl(D_{Q_p^+,p}(H_\star)-D_{Q_p^-,p}(H_\star)\bigr)
=-2a+o(1).
\tag{10}
\]
Therefore (7) proves the distinct endpoint conclusion
\[
\boxed{\quad
\frac L{\sqrt p}
\bigl(\Theta_{Q_p^+}-\Theta_{Q_p^-}\bigr)
=2a+o(1).
\quad}\tag{11}
\]
The sign agrees with the explicit transport: moving the real labels
right increases their logarithmic weights while decreasing the
remaining triangular moment. It is not a perturbation of integer
prime identities: the new labels need not be integers or primes.

Thus the scale \(\sqrt p/L\) is **sharp for the two-source
Chebyshev-fidelity requirement in this particular matched class**.
Matching the endpoint Chebyshev increment only to
\(O(\sqrt p/L)\), even with exact cardinality and exact CA-prefix
agreement and a uniform all-start counting envelope, permits a
nonvanishing critical signed-moment discrepancy. An
\(o(\sqrt p/L)\) *difference* is sufficient and, by (8), necessary
for the two sources to be indistinguishable to first order by this
moment. The example does not assert that two different sets of
ordinary primes can obey the same constraints.

## 4. Audit, prior art, and limitation

The identity (3) is elementary Taylor/Abel-summation algebra, and
integrated prime-counting errors (first Riesz/Cesàro means) and
Chebyshev prime-weight sums are classical. No general novelty is
claimed for those constructions. Guth and Maynard, *New large value
estimates for Dirichlet polynomials*, *Annals of Mathematics* 203
(2026), 623–675, Corollary 1.3, supplies the external short-interval
envelope; its role and bibliographic data already appear in this
line's SOURCES.md. The line-specific mathematical consequence is
the precise **joint endpoint-fidelity threshold**, together with its
sharpness by the independently constructed RE-254 control at a
CA-selected critical horizon.

Decisive sign and scaling checks: (i) the baseline in \(D\) is
\(-H^2/(2L)\), while the correction in \(\mathcal E\) is
\(+H^2/(2pL)\); (ii) moving one shell label right strictly raises
\(\Theta\) and lowers \(D\); (iii) equality of shell **counts**
is essential for replacing \(\Delta\mathcal E\) by
\(\Delta\Theta\); (iv) \(H_\star=p^{3/4+o(1)}\), so
\(H_\star^3/p^{5/2}=o(1)\); (v) no unproved assertion that CA selection
controls the *future* Chebyshev shell is used. A finite exact-algebra
control with displaced real labels can check (3) term by term
without treating floating-point cancellation as proof.

The theorem characterizes the information **still missing**, not a
new bound for actual prime gaps or for the selected Chebyshev
increment. It does not prove that
\(\mathcal E_{P,p}(H_\star)=o(\sqrt p/L)\), nor control the remote
annulus or the Euler-product/Robin normalization, nor prove RH.
An independent adversarial review is still required before treating
the derived sharp boundary as fully audited.
