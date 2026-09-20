# MC-416 — Weighted positive van der Corput filters cannot remove the diagonal

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-415` leaves open the possibility that a signed or oscillatory shift weight might avoid the zero-shift cost that re-squares the linear sieve under ordinary Fejér/van der Corput averaging. At the level of a single positive quadratic shift energy, that escape is not available.

Let

\[
a_n=0\quad(n\notin[1,N]),
\qquad
S=\sum_n a_n,
\qquad
C_h=\sum_n a_{n+h}\overline{a_n}.
\tag{1}
\]

Fix complex shift coefficients `c_0,...,c_(H-1)` and write

\[
\sigma_c:=\sum_{j=0}^{H-1}c_j,
\qquad
K_c(h):=\sum_{\substack{0\le j,k<H\\j-k=h}}
c_j\overline{c_k}.
\tag{2}
\]

Then the weighted sliding-window energy has the exact correlation expansion

\[
\boxed{
E_c
:=
\sum_{t\in\mathbb Z}
\left|\sum_{j=0}^{H-1}c_j a_{t+j}\right|^2
=
\sum_{|h|<H}K_c(h)C_h.
}
\tag{3}
\]

Its diagonal coefficient is

\[
\boxed{
K_c(0)=\sum_{j=0}^{H-1}|c_j|^2>0
}
\tag{4}
\]

for every nonzero filter. In particular, changing signs or phases of the linear shift weights does not cancel the diagonal after the norm square is expanded.

If the filter is to recover the original sum by the same translation-invariant averaging step, one needs `sigma_c != 0`. Since

\[
\sum_t\sum_j c_j a_{t+j}=\sigma_c S,
\tag{5}
\]

and at most `N+H-1` sliding windows are nonzero, Cauchy gives

\[
\boxed{
|S|^2
\le
\frac{N+H-1}{|\sigma_c|^2}
\sum_{|h|<H}K_c(h)C_h.
}
\tag{6}
\]

The normalized zero-shift coefficient in `(6)` is therefore

\[
(N+H-1)\frac{K_c(0)}{|\sigma_c|^2}.
\tag{7}
\]

Cauchy--Schwarz on the coefficient vector itself yields

\[
|\sigma_c|^2
\le
H\sum_{j=0}^{H-1}|c_j|^2
=
H K_c(0),
\tag{8}
\]

hence

\[
\boxed{
(N+H-1)\frac{K_c(0)}{|\sigma_c|^2}
\ge
\frac{N+H-1}{H}.
}
\tag{9}
\]

Equality holds exactly when all `c_j` are equal up to one common scalar. Thus the ordinary constant sliding window underlying the Fejér kernel in `MC-415` already **minimizes the normalized diagonal burden among all `H`-slot linear filters that reconstruct `S` through `(5)`**. A genuinely oscillatory choice makes the diagonal coefficient strictly worse unless it is merely a common phase/scaling of the constant filter.

There is a representation-free version of the same obstruction. The autocorrelation kernel `K_c` is positive definite. More generally, every Hermitian positive-definite shift kernel `K` satisfies

\[
|K(h)|\le K(0)
\tag{10}
\]

from the `2 x 2` principal minor on `{0,h}`. Consequently

\[
\boxed{
K(0)=0\ \Longrightarrow\ K(h)=0\ \text{for all }h.
}
\tag{11}
\]

So a nontrivial diagonal-free shift kernel is necessarily **indefinite**; it cannot itself be a positive norm-square energy used directly on the right side of Cauchy/van der Corput.

Applied to the well-factorable upper-sieve sequence of `MC-409`--`MC-415`, this closes one specific escape from the re-squared lcm diagonal: replacing the standard triangular Fejér average by signed or oscillatory **linear filter coefficients before squaring** cannot reduce, let alone annihilate, the zero-shift `C_0` cost. The surviving possibilities must change something more substantial: exploit the off-diagonal correlations strongly enough to compensate for the diagonal, use an indefinite signed correlation identity controlled by additional arithmetic information, or perform a modulus-factorized/nonstationary `A`-process that changes the object before the positive quadratic closure.

No improved character-sum estimate, source-depth exponent, Mertens bound, or RH consequence follows.

## 1. Exact weighted shift identity

Put

\[
B_t:=\sum_{j=0}^{H-1}c_j a_{t+j}.
\tag{12}
\]

Then

\[
\begin{aligned}
\sum_t|B_t|^2
&=
\sum_t\sum_{j,k}c_j\overline{c_k}
 a_{t+j}\overline{a_{t+k}}\\
&=
\sum_{j,k}c_j\overline{c_k}
\sum_n a_{n+j-k}\overline{a_n}\\
&=
\sum_{|h|<H}
\left(
\sum_{j-k=h}c_j\overline{c_k}
\right)C_h,
\end{aligned}
\tag{13}
\]

which is `(3)`.

The `h=0` contribution is exactly

\[
K_c(0)C_0
=
\left(\sum_j|c_j|^2\right)
\left(\sum_n|a_n|^2\right).
\tag{14}
\]

No relative phase between the `c_j` survives here. This is the precise reason that a signed filter does not create a signed diagonal after squaring.

## 2. Reconstructing the global sum fixes the optimal diagonal ratio

Summing `(12)` over all `t` and using zero extension gives `(5)` exactly. The possible nonzero `t` lie in an interval of length at most `N+H-1`, so Cauchy gives

\[
|\sigma_c S|^2
\le
(N+H-1)E_c,
\tag{15}
\]

which is `(6)`.

Now normalize the filter by its DC response `sigma_c`. Scaling every `c_j` by the same complex scalar leaves

\[
\frac{K_c(0)}{|\sigma_c|^2}
\tag{16}
\]

unchanged. Equation `(8)` proves that the smallest possible value of `(16)` is `1/H`, attained by the constant vector.

This is stronger than merely saying that every positive window has a diagonal. Within this entire one-filter/Cauchy architecture, the standard equal-weight window already gives the **least possible normalized diagonal coefficient**. An oscillatory filter can reshape the off-diagonal kernel `K_c(h)`, but it cannot purchase that reshaping by reducing the diagonal cost.

If some endpoint coefficients vanish, one should first trim the filter to its actual span. If only `m` coefficients are nonzero, the sharper coefficient-count inequality `|sigma_c|^2<=m K_c(0)` applies. Thus sparse signing does not evade the conclusion either.

## 3. Positive-definite kernels force a nonzero zero shift

For completeness, `K_c` is positive definite because for any finitely supported complex sequence `(z_r)`,

\[
\begin{aligned}
\sum_{r,s}K_c(r-s)z_r\overline{z_s}
&=
\sum_j
\left|
\sum_r z_r c_{j+r}
\right|^2
\ge0,
\end{aligned}
\tag{17}
\]

with harmless reindexing outside the finite support.

The broader statement `(10)` does not require an autocorrelation representation. If `K` is Hermitian positive definite, then

\[
\begin{pmatrix}
K(0)&K(h)\\
\overline{K(h)}&K(0)
\end{pmatrix}
\tag{18}
\]

is positive semidefinite. Its determinant is nonnegative, giving

\[
K(0)^2-|K(h)|^2\ge0.
\tag{19}
\]

Hence `(10)` and `(11)`.

This identifies the exact price of trying to delete the zero shift. A nontrivial kernel with zero diagonal cannot be positive definite, so its correlation form can take both signs. Such a kernel may still be useful if another arithmetic identity controls that indefinite form, but positivity/Cauchy alone no longer supplies the upper bound.

## 4. Relation to the lcm diagonal in the well-factorable frame

For the `MC-409` sequence

\[
a_n=w(n)\chi(n),
\qquad
w(n)=\sum_{d\mid n}\lambda_d,
\tag{20}
\]

`MC-415` proves

\[
C_0
=
\sum_n|w(n)\chi(n)|^2
\tag{21}
\]

and rewrites it as the Selberg/lcm quadratic form

\[
\sum_{d,e}
\frac{\lambda_d\overline{\lambda_e}}{[d,e]}
\tag{22}
\]

up to the explicit conductor-coprimality density and finite counting error recorded there.

Combining `(9)` with `MC-415` shows that a weighted one-filter van der Corput step cannot make the coefficient of this re-squared lcm object smaller than the ordinary equal-window coefficient merely by choosing phases or signs in the shift weights. The only quantity those phases can alter is the off-diagonal mixture

\[
\sum_{0<|h|<H}K_c(h)C_h.
\tag{23}
\]

Therefore a weighted-filter continuation is viable only if `(23)` is controlled in a way that produces a net gain despite the unchanged-or-larger normalized diagonal. That is a genuinely stronger obligation than “choose oscillatory shift weights to cancel `h=0`.”

## 5. Prior-art and novelty boundary

No novelty is claimed for the underlying inequalities. The finite van der Corput inequality is a classical Cauchy--Schwarz correlation argument; `MC-415` already records N. Edeko, H. Kreidler and R. Nagel, *A dynamical proof of the van der Corput inequality*, Dynamical Systems **37** (2022), 1805--1825, DOI `10.1080/14689367.2022.2100244`, arXiv:`2106.11835`, as a modern reference for Hilbert-space variants.

The facts that autocorrelation kernels are positive definite, that a nonzero positive-definite kernel has positive value at zero, and that `(8)` is optimized by constant coefficients are standard Hilbert-space/Fourier analysis. Equations `(3)`--`(11)` are derived directly here and do not rely on an unverified literature theorem.

A targeted literature audit on 20 September 2026 found the weighted/positive-kernel ingredients as classical van der Corput, Cauchy--Schwarz, autocorrelation, and Herglotz/positive-definite-kernel structure; no novelty claim is made for their combination as an abstract theorem. The durable contribution is the local frontier classification relative to `MC-415`: the previously open “signed/oscillatory shift filter” escape does not remove the lcm diagonal as long as the method remains a positive sliding-filter energy with the usual global-sum reconstruction.

## Boundaries and falsification tests

- **This does not classify every signed correlation argument.** One may form an indefinite linear combination of the `C_h` with zero coefficient at `h=0`; `(11)` says only that such a kernel is not positive definite and therefore is not itself a norm-square upper bound.
- **This does not rule out off-diagonal compensation.** A nonconstant filter may worsen the normalized diagonal while producing more favorable arithmetic cancellation in `(23)`. Such a gain must be proved after the actual sieve/source bookkeeping.
- **This does not classify modulus-factorized q-van der Corput.** If an `A`-process changes the modulus, support, or arithmetic variables before the positive quadratic step, the relevant diagonal may be a different object. The present result applies to one translation-invariant filter acting on the fixed sequence `(a_n)`.
- **This does not classify nonstationary or boundary-sensitive operators.** The proof uses a fixed shift filter and the uniform reconstruction `(5)`. A genuinely different operator must expose its own reconstruction and diagonal exactly rather than being rejected by analogy.
- **Zero DC response is not an escape inside this architecture.** If `sigma_c=0`, then `(5)` contains no information about `S`; the filter annihilates the global constant mode. Recovering `S` would require an additional operation whose cost must be accounted for separately.
- **The standard Fejér filter is optimal only for diagonal ratio, not for the full bound.** Equation `(9)` does not assert that equal weights minimize the total right side of `(6)` for a specific arithmetic sequence.
- **No RH-scale input is used.** The argument is finite linear algebra, shift correlation, and Cauchy--Schwarz.

## Consequence for the research line

The surviving `MC-409`--`MC-415` route is narrower again. The incomplete translated off-diagonal family remains live, but a cheap attempt to rescue it by replacing the triangular shift average with signed or oscillatory **pre-square filter coefficients** cannot reduce the re-squared lcm diagonal. The equal-weight Fejér window is already extremal for that diagonal ratio.

The next useful calculation must therefore do one of two things: derive a real collective estimate for the incomplete translated off-diagonal strong enough to offset the unavoidable diagonal budget, or introduce a different arithmetic `A`-process/indefinite identity whose diagonal structure is genuinely changed and whose lost positivity is replaced by another controlled mechanism. Merely reweighting the same positive shift energy is now closed.