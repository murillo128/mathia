# PC-136 — cross-shell-only primorial Hessian has universal bulk spectrum with Mertens-squared defect

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` for the canonical resultant-only all-divisor Hessian aggregate along the minimal common refinement containing every prime shell up to a cutoff. PC-135 showed that adding both same-shell discriminant Hessians and cross-shell resultant Hessians with coefficient one reconstructs the universal full-polygon inverse-square Laplacian exactly, but deliberately left open the natural repair in which the within-shell discriminant pieces are omitted. That repair does retain arithmetic labels at every finite conductor. Nevertheless, on the primorial refinement forced by putting all prime layers up to `x` into one polygon, its **normalized empirical spectrum converges to the same universal law as the full regular polygon**. The exact Wasserstein-1 distance is an elementary Euler product asymptotic to a constant times the square of the classical Mertens prime product.

This does not identify individual eigenvalues or rule out extreme/outlier statistics, non-bulk renormalizations, selective weighted divisor pairs, Schur complements, or genuinely non-Cauchy operators. It does rule out the most canonical cross-shell-only growing aggregate as a source of a new bulk spectral law or critical-line density.

## 1. Resultant-only Hessian and the omitted internal energy

For `N>1`, write the exact-order partition

\[
\mu_N=\bigsqcup_{d\mid N}S_d,
\qquad S_d=P_d^*.
\]

Let `H_N^\times` be the weighted graph Laplacian obtained by retaining the PC-128 inverse-square chord edge

\[
c(x,y)=\frac1{|x-y|^2}
\]

**only when `x` and `y` lie in distinct exact-order shells**. Equivalently,

\[
\boxed{
H_N^\times
=\sum_{\substack{d<e\\d,e\mid N}}H_{d,e},
}
\]

where `H_{d,e}` is the vertexwise Hessian of the logarithmic resultant interaction between `P_d^*` and `P_e^*`. This is the canonical all-divisor aggregate built from pairwise resultants alone, with the same-shell discriminant energies deliberately omitted.

Let `L_N` be the full inverse-square chord Laplacian of the regular `N`-gon, as in PC-032 and PC-135. If `L_d^{\rm int}` denotes the Laplacian using only edges whose two endpoints lie in `P_d^*`, embedded on the corresponding coordinates of `mu_N`, then edge partitioning gives the exact operator identity

\[
\boxed{
L_N-H_N^\times
=\bigoplus_{d\mid N}L_d^{\rm int}\succeq0.
}
\]

Thus the cross-shell-only aggregate is not equal to the universal polygon operator at finite `N`, but its entire departure is the positive semidefinite sum of the omitted within-shell energies.

## 2. Exact trace of one primitive-shell internal Laplacian

Index `P_n^*` by the reduced residues `U(n)`. The trace of its internal Laplacian is

\[
T^*(n)
:=\operatorname{tr}L_n^{\rm int}
=\sum_{\substack{a,b\in U(n)\\a\ne b}}
\frac1{4\sin^2\!\bigl(\pi(a-b)/n\bigr)}.
\]

For a nonzero residue `h mod n`, let

\[
r_n(h)
:=\#\{a\bmod n:(a,n)=(a-h,n)=1\}.
\]

Writing `R=rad(n)`, CRT gives independently at every prime power `p^e||n`

\[
\#\{a\bmod p^e:p\nmid a(a-h)\}
=
\begin{cases}
p^{e-1}(p-1),&p\mid h,\\
p^{e-1}(p-2),&p\nmid h.
\end{cases}
\]

Hence

\[
\boxed{
r_n(h)=\frac nR
\prod_{p\mid R}\bigl((p-2)+\mathbf1_{p\mid h}\bigr).}
\]

Expand the product over divisors `q|R`. The classical regular-polygon cosecant identity

\[
\sum_{k=1}^{M-1}\frac1{4\sin^2(\pi k/M)}
=\frac{M^2-1}{12}
\]

then yields

\[
\begin{aligned}
T^*(n)
&=\frac{n/R}{12}
\sum_{q\mid R}
\left(\prod_{p\mid R/q}(p-2)\right)
\left[\left(\frac nq\right)^2-1\right]\\
&=\boxed{
\frac1{12}
\left[
 n^3\prod_{p\mid n}
 \left(1-\frac2p+\frac1{p^3}\right)
 -\varphi(n)
\right].
}
\end{aligned}
\]

The formula includes the edge cases automatically: `T^*(1)=T^*(2)=0`. For a prime `p`, it becomes

\[
T^*(p)=\frac{(p^2-1)(p-2)}{12},
\]

which is exactly the internal energy of the `p-1` non-anchor vertices; the complementary anchor star has trace `(p^2-1)/6`, agreeing with PC-035.

## 3. The all-divisor trace defect is multiplicative

Define

\[
a(n):=\prod_{p\mid n}
\left(1-\frac2p+\frac1{p^3}\right),
\qquad
F(N):=\sum_{d\mid N}d^3a(d).
\]

Summing the omitted within-shell traces and using the classical identity `sum_{d|N} phi(d)=N` gives

\[
\boxed{
\operatorname{tr}(L_N-H_N^\times)
=\sum_{d\mid N}T^*(d)
=\frac{F(N)-N}{12}.
}
\]

Since the full regular-polygon spectrum is

\[
\lambda_k(L_N)=\frac{k(N-k)}2,
\qquad 0\le k<N,
\]

one has `tr L_N=(N^3-N)/12` and therefore

\[
\boxed{
\operatorname{tr}H_N^\times
=\frac{N^3-F(N)}{12}.
}
\]

The function `F` is multiplicative. For `p^e||N`,

\[
\boxed{
F(p^e)
=1+
\frac{(p^3-2p^2+1)(p^{3e}-1)}{p^3-1}.
}
\]

In particular, for squarefree `N`,

\[
\boxed{
\frac{F(N)}{N^3}
=\prod_{p\mid N}
\left(1-\frac2p+\frac2{p^3}\right).
}
\]

Exact controls are small and nontrivial. For `N=6`, `F(6)=22`, so the omitted trace is `4/3` and `tr H_6^times=97/6`. For `N=30`, `F(30)=1694`, so the omitted trace is `416/3` and

\[
\operatorname{tr}H_{30}^\times=\frac{12653}{6}.
\]

Direct construction of the weighted cross-shell Laplacians gives these same values.

## 4. Exact Wasserstein distance between the two spectra

Let the eigenvalues of `H_N^times` and `L_N`, in increasing order, be respectively

\[
\mu_0\le\cdots\le\mu_{N-1},
\qquad
\lambda_0\le\cdots\le\lambda_{N-1},
\]

and define the normalized empirical spectral measures

\[
\nu_N^\times
:=\frac1N\sum_{j=0}^{N-1}\delta_{\mu_j/N^2},
\qquad
\nu_N^{\rm full}
:=\frac1N\sum_{j=0}^{N-1}\delta_{\lambda_j/N^2}.
\]

Because `L_N-H_N^times` is positive semidefinite, the min-max principle gives

\[
\mu_j\le\lambda_j
\qquad(0\le j<N).
\]

For equally weighted measures on the real line, the monotone coupling is optimal for Wasserstein-1. Since every ordered difference has the same sign,

\[
\begin{aligned}
W_1(\nu_N^\times,\nu_N^{\rm full})
&=\frac1{N^3}\sum_{j=0}^{N-1}(\lambda_j-\mu_j)\\
&=\frac{\operatorname{tr}(L_N-H_N^\times)}{N^3}.
\end{aligned}
\]

Therefore the spectral distance is not merely bounded by the omitted trace; it is **exactly**

\[
\boxed{
W_1(\nu_N^\times,\nu_N^{\rm full})
=\frac{F(N)-N}{12N^3}.
}
\]

This turns the question of bulk spectral survival into a completely explicit multiplicative arithmetic function.

## 5. Primorial refinement collapses to the universal polygon law

The minimal regular polygon containing every prime shell `P_p^*` with `p<=x` as literal sublayers is the primorial conductor

\[
N_x:=\prod_{p\le x}p.
\]

This is therefore the canonical common-refinement sequence for simultaneously retaining all prime layers up to a cutoff. Since `N_x` is squarefree,

\[
\boxed{
W_1(\nu_{N_x}^\times,\nu_{N_x}^{\rm full})
=\frac1{12}
\left[
\prod_{p\le x}
\left(1-\frac2p+\frac2{p^3}\right)
-\frac1{N_x^2}
\right].
}
\]

Factor the local term as

\[
1-\frac2p+\frac2{p^3}
=\left(1-\frac1p\right)^2q_p,
\]

where

\[
q_p
=\frac{p^3-2p^2+2}{p(p-1)^2}
=1-\frac{p-2}{p(p-1)^2}.
\]

Because `sum_p (1-q_p)<infinity`, the product

\[
C:=\prod_pq_p
\]

converges to a positive constant. Mertens' classical prime-product theorem gives

\[
\prod_{p\le x}\left(1-\frac1p\right)
\sim\frac{e^{-\gamma}}{\log x}.
\]

Consequently

\[
\boxed{
W_1(\nu_{N_x}^\times,\nu_{N_x}^{\rm full})
\sim
\frac{Ce^{-2\gamma}}{12(\log x)^2}
\longrightarrow0.
}
\]

PC-135 already proved

\[
\nu_N^{\rm full}
\Longrightarrow
\left(t\mapsto\frac{t(1-t)}2\right)_*dt,
\]

with density

\[
\frac4{\sqrt{1-8y}}\,\mathbf1_{(0,1/8)}(y)\,dy.
\]

The exact Wasserstein collapse therefore forces the same limit for the resultant-only operator:

\[
\boxed{
\nu_{N_x}^\times
\Longrightarrow
\frac4{\sqrt{1-8y}}\,\mathbf1_{(0,1/8)}(y)\,dy.
}
\]

Thus deleting **all** same-shell discriminant Hessians preserves nontrivial arithmetic at each finite conductor, but on the natural all-primes common refinement it does not change the normalized bulk spectral law.

## 6. Prior-art and novelty audit

No theorem-level novelty is claimed for the ingredients. The `csc^2` full-polygon spectrum and trigonometric sum are classical and already anchored through Calogero--Perelomov in `SOURCES.md`. Counting simultaneous reduced residues prime by prime is elementary CRT/inclusion-exclusion, while `sum_{d|N}phi(d)=N` is standard multiplicative number theory. The asymptotic prime product is Mertens' classical third theorem; modern standard references include G. Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory*, 3rd ed., GSM 163, AMS, 2015. Mertens-product error terms and their relation to prime-distribution questions are themselves a mature analytic-number-theory subject, so their appearance here cannot be treated as a new zeta mechanism.

Directed searches for reduced-residue cosecant-square energies, primitive-root Riesz energies, and cross-shell roots-of-unity inverse-square aggregates did not expose this exact Prime-Circle trace/Wasserstein specialization. That absence is not evidence of historical priority. The durable contribution is the scope classification: the specific growing operator left open by PC-135 has an exact spectral-distance defect that reduces to a standard Euler product, and its primorial bulk limit forgets the exact-order partition.

The Mertens-squared factor is especially important as a novelty control. One could take its Mellin/Dirichlet transforms, study its fine error term, or rewrite the prime product through zeta-related analytic machinery, but that would be importing the already-classical prime-product route after the geometric spectrum has collapsed. It does not supply an intrinsic functional equation, gamma factor, critical-line involution, or new zero divisor.

## 7. Boundary and consequences for the RH search

The result closes the most canonical omission repair to PC-135 at the level of normalized bulk spectrum:

\[
\boxed{
\text{all cross-shell resultant Hessians only}
\;\xrightarrow[\text{primorial refinement}]{}\;
\text{universal full-polygon bulk spectrum}
}
\]

with the entire Wasserstein discrepancy measured by a Mertens-squared Euler product. Therefore an apparent limiting spectral density from this construction cannot be counted as new RH structure; the arithmetic birth labels survive only in a vanishing bulk perturbation on this refinement.

The statement is deliberately narrower than an operator-norm no-go. Trace/Wasserstein collapse does **not** imply that the largest few eigenvalues, eigenvectors, edge-localized modes, spectral edges, or a suitably amplified subleading statistic are universal. It also does not cover weighted divisor-pair aggregates, omission rules other than `same shell versus different shell`, Schur/Kron reduction before aggregation, non-polynomial functional calculus, or cross-level constructions that retain the family `{H_N^times}` rather than only its empirical bulk spectrum. Along fixed-prime power towers the cross-shell trace fraction does not vanish to one in the same way, so the primorial conclusion must not be silently generalized to every refinement path.

The exact falsification tests are immediate: construct `H_N^times` for arbitrary `N`, verify the PSD decomposition against `L_N`, check the displayed `T^*(n)` formula shell by shell, verify `tr H_N^times=(N^3-F(N))/12`, and compare the ordered normalized spectra to confirm the exact Wasserstein identity. Any failure of one of those finite equalities would refute the derivation before asymptotics enter.
