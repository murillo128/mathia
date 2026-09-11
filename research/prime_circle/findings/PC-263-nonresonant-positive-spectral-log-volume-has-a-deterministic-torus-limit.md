# PC-263 — nonresonant positive spectral log-volume has a deterministic torus limit

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-BOUNDARY` for the zero-energy logarithmic-volume part of the nonresonant long shared-upper cocycle left open explicitly by PC-262.

Let

\[
2<p_n<r_n<q_n
\]

be distinct primes with `q_n -> infinity`, and assume

\[
\alpha_n=\frac{p_n}{q_n}\to\alpha,
\qquad
\beta_n=\frac{r_n}{q_n}\to\beta,
\qquad
0<\alpha<\beta<1,
\]

with `1,alpha,beta` linearly independent over `Q`, exactly as in PC-262. For the natively normalized shared-upper defect

\[
\Delta_n=\frac{D_{p_n,r_n;q_n}}{q_n\sqrt{p_nr_n}},
\]

write `k_n=rank Delta_n` and let `sigma_{n,1},...,sigma_{n,k_n}` be its positive singular values. Then the positive spectral log-volume has a deterministic limit:

\[
\boxed{
\frac1{k_n}\log\operatorname{pdet}(\Delta_n\Delta_n^*)
=\frac1{k_n}\sum_{a=1}^{k_n}\log\sigma_{n,a}^2
\longrightarrow
\mathcal L(\alpha,\beta).
}
\tag{1}
\]

The limit is determined entirely by the same induced Haar torus-return process that gives the bulk IDS in PC-262. More precisely,

\[
\boxed{
\mathcal L(\alpha,\beta)
=
\log(\alpha\beta)-6
+\Gamma_p(\alpha,\beta)
+\Gamma_r(\alpha,\beta),
}
\tag{2}
\]

where `Gamma_p` and `Gamma_r` are the deterministic per-collision logarithmic run factors of the two selected path-edge processes. In particular, the potentially dangerous singular Green-weight term has the explicit universal mean

\[
\boxed{
\frac1{k_n}\sum_{a=1}^{k_n}\log\rho_{n,a}
\longrightarrow
\frac12\log(\alpha\beta)-3,
}
\tag{3}
\]

where `rho_{n,a}=w_{n,a}/(q_n sqrt(p_nr_n))` is the PC-258 normalized collision weight.

Thus the weak bulk convergence of PC-262 can be strengthened at the singular test function `log x` **for the zero-energy positive pseudodeterminant**, despite the accumulation risk at zero. The reason is not a generic theorem about weak convergence: it is the exact PC-254 factorization plus a source-forced boundary-strip count that gives uniform integrability of the logarithmic Green singularity. The same limit is reproduced by admissible pairwise-coprime rational-partition controls with the same irrational limiting ratios. This closes the natural normalized positive log-determinant/log-volume escape, but it does **not** prove universality of the top Lyapunov exponent, shifted determinants, edge outliers, fine spacing, or other genuinely global transfer-cocycle observables.

## 1. PC-254 reduces the positive determinant exactly

Use the PC-251/PC-254 collision factorization

\[
\Delta_n=-U_nR_nV_n^T,
\qquad
R_n=\operatorname{diag}(\rho_{n,1},\ldots,\rho_{n,k_n}),
\tag{4}
\]

with selected-path Gram matrices

\[
G_{p,n}=U_n^TU_n,
\qquad
G_{r,n}=V_n^TV_n.
\tag{5}
\]

PC-254 proves the exact finite identity

\[
\boxed{
\operatorname{pdet}(\Delta_n\Delta_n^*)
=
\left(\prod_{a=1}^{k_n}\rho_{n,a}^2\right)
\det G_{p,n}\det G_{r,n}.
}
\tag{6}
\]

If `R_{p,n}` and `R_{r,n}` denote the maximal runs of consecutive selected path edges on the two lower grids, then

\[
\det G_{p,n}=\prod_{R\in\mathcal R_{p,n}}(|R|+1),
\qquad
\det G_{r,n}=\prod_{S\in\mathcal R_{r,n}}(|S|+1).
\tag{7}
\]

Therefore

\[
\frac1{k_n}\log\operatorname{pdet}(\Delta_n\Delta_n^*)
=
\frac{2}{k_n}\sum_{a=1}^{k_n}\log\rho_{n,a}
+
\frac1{k_n}\sum_R\log(|R|+1)
+
\frac1{k_n}\sum_S\log(|S|+1).
\tag{8}
\]

PC-254 already shows that no phase or cancellation survives in this compression. What PC-262 left open was whether the singular logarithm could nevertheless retain sequence-dependent information invisible to weak bulk convergence. Equation (8) isolates the only three places where that could occur.

## 2. The logarithmic Green weight has an explicit Haar mean

PC-258 identifies a collision with a return of

\[
T_{\alpha_n,\beta_n}(x,y)=(x+\alpha_n,y+\beta_n)\pmod1
\]

to

\[
W_{\alpha_n,\beta_n}
=[1-\alpha_n,1)\times[1-\beta_n,1),
\]

and gives

\[
\rho_n(x,y)
=
\sqrt{\alpha_n\beta_n}\,
G\!\left(
\frac{1-x}{\alpha_n},
\frac{1-y}{\beta_n}
\right),
\qquad
G(u,v)=\min(u,v)-uv.
\tag{9}
\]

Conditioned on Haar measure in the limiting collision rectangle, the affine coordinates `U,V` in (9) are independent uniform variables on `[0,1]`. Since

\[
G(U,V)=\min(U,V)\,[1-\max(U,V)],
\tag{10}
\]

symmetry across `U=V` gives

\[
\begin{aligned}
\mathbb E\log G(U,V)
&=2\int_0^1\int_u^1
\bigl(\log u+\log(1-v)\bigr)\,dv\,du\\
&=-3.
\end{aligned}
\tag{11}
\]

Hence the candidate conditional Haar average is

\[
\boxed{
\mathbb E\log\rho
=\frac12\log(\alpha\beta)-3.
}
\tag{12}
\]

For bounded truncations of `log rho`, PC-258/PC-262 equidistribution already implies convergence to (12). The only missing point is uniform integrability near the four boundary pieces where `G` vanishes.

## 3. Exact grid counting controls the logarithmic singularity

Put

\[
a=\min(U,V),
\qquad
b=1-\max(U,V),
\]

so `G(U,V)=ab`. If `0<delta<1`, then

\[
G(U,V)\le\delta
\quad\Longrightarrow\quad
 a\le\sqrt\delta
\ \text{or}\ 
 b\le\sqrt\delta.
\tag{13}
\]

Thus a small Green weight forces at least one of `U,V` into a boundary strip of width `sqrt(delta)`.

This is where the finite rational source gives more than abstract equidistribution. Because `gcd(p_n,q_n)=gcd(r_n,q_n)=1`, each coordinate sequence

\[
\{u p_n/q_n\},
\qquad
\{u r_n/q_n\},
\qquad 0\le u<q_n,
\]

is exactly a permutation of the `q_n`-grid. A strip of width `epsilon` in the `U` coordinate therefore contains at most `alpha_n q_n epsilon+O(1)` raw orbit points, and similarly for the other three relevant strips. Restricting to collision points can only decrease the count. Consequently, for all sufficiently large `n`,

\[
\boxed{
\#\{a:G(U_{n,a},V_{n,a})\le\delta\}
\le 4q_n\sqrt\delta+O(1).
}
\tag{14}
\]

PC-258 gives `k_n/q_n -> alpha beta`, so after division by `k_n`,

\[
\frac1{k_n}
\#\{a:\rho_{n,a}\le e^{-t}\}
\le C_{\alpha,\beta}e^{-t/2}+O(q_n^{-1})
\tag{15}
\]

uniformly for the relevant range of `t`, after absorbing the fixed factor `sqrt(alpha_n beta_n)`.

There is also an exact finite lower cutoff. The unnormalized PC-251 collision weights are positive integers, so `w_{n,a}>=1`. Since `p_n,r_n<q_n`,

\[
\rho_{n,a}
=\frac{w_{n,a}}{q_n\sqrt{p_nr_n}}
\ge\frac1{q_n^2}.
\tag{16}
\]

Integrating the tail bound (15) only up to `2 log q_n` therefore gives, for every truncation level `M`,

\[
\limsup_{n\to\infty}
\frac1{k_n}
\sum_a
\bigl(-\log\rho_{n,a}-M\bigr)_+
\le C_{\alpha,\beta}e^{-M/2}.
\tag{17}
\]

The logarithms are uniformly integrable. Bounded-truncation equidistribution may now be followed by `M->infinity`, proving (3) and the explicit value (12).

This step is essential. Weak convergence of the singular-value histogram alone does not justify integrating `log x`; the source-forced grid bound (14) is what removes that gap for the collision-weight contribution.

## 4. The two path-run factors also have deterministic limits

It remains to treat the two terms in (8) coming from (7). A run on the `p` side is a string of consecutive `p`-boundary cells that all collide with an `r` boundary. In PC-258 torus coordinates a `p` boundary means

\[
x\in[1-\alpha,1),
\]

while a `p` boundary that is **not** a collision lies in the nonempty open set

\[
A_p=
(1-\alpha,1)\times(0,1-\beta).
\tag{18}
\]

Because `1,alpha,beta` are rationally independent, the limiting torus translation is minimal. Visits to any fixed nonempty open set are syndetic: by compactness, finitely many inverse iterates of a smaller closed rectangle inside `A_p` cover the torus. The same finite cover is stable for all sufficiently close rational approximants `(alpha_n,beta_n)`, exactly as in the robust-return argument of PC-262. Hence there is a constant `L_p(alpha,beta)` such that every sufficiently large finite approximant has no `p`-side collision run longer than `L_p`.

The identical argument with

\[
A_r=(0,1-\alpha)\times(1-\beta,1)
\tag{19}
\]

gives a uniform bound `L_r(alpha,beta)` for the `r`-side runs.

With these bounds, the run determinant is no longer a genuinely unbounded functional. For each `1<=ell<=L_p`, the event that a maximal `p`-run has length `ell` is determined by a fixed finite raw torus window; PC-262's robust return bound converts the required finite number of boundary/collision events into a uniformly bounded raw window. Its empirical frequency therefore converges to a deterministic Haar cylinder frequency. The same holds on the `r` side.

If `N_{p,n}(ell)` and `N_{r,n}(ell)` denote the numbers of maximal runs of length `ell`, define

\[
\Gamma_p(\alpha,\beta)
=
\lim_{n\to\infty}
\frac1{k_n}
\sum_{\ell=1}^{L_p}
N_{p,n}(\ell)\log(\ell+1),
\tag{20}
\]

\[
\Gamma_r(\alpha,\beta)
=
\lim_{n\to\infty}
\frac1{k_n}
\sum_{\ell=1}^{L_r}
N_{r,n}(\ell)\log(\ell+1).
\tag{21}
\]

Both limits exist and depend only on the induced Haar torus process and the limiting ratios. Equations (7), (20), and (21) are exactly the two remaining terms in (8).

Combining them with (3) proves (1)--(2).

## 5. The result is stronger than bulk weak convergence but weaker than a Lyapunov no-go

PC-262 proves weak convergence of the singular-square empirical measure. Since the limiting measure may accumulate at zero, `log x` is outside the class of continuous bounded test functions and its integral need not follow from that theorem. PC-263 supplies the missing zero-energy control for the **positive** spectral volume by exploiting the special factorization (6).

Equivalently, the geometric mean of the positive squared singular values has the deterministic limit

\[
\boxed{
\left(
\operatorname{pdet}(\Delta_n\Delta_n^*)
\right)^{1/k_n}
\longrightarrow
\alpha\beta\,e^{-6}
\exp\!\bigl(\Gamma_p(\alpha,\beta)+\Gamma_r(\alpha,\beta)\bigr).
}
\tag{22}
\]

This is a noncontinuous spectral statistic, but it is still classical induced-torus data.

The conclusion must not be overextended. The transfer matrices of PC-257 contain more information than their determinant. Top Lyapunov exponents, norms of long products, rotation/winding data, shifted characteristic determinants, and rare edge outliers are subadditive or genuinely global quantities and are not reduced by (6). General multiplicative-ergodic theory for uniquely ergodic systems, including Furman's theorem, is a warning that such cocycle questions are distinct from additive determinant averages. PC-263 closes only the determinant/Lyapunov-**sum** channel selected by the positive pseudodeterminant.

## 6. Prior-art and novelty audit

The abstract ingredients are classical. PC-262 already anchors unique/strict ergodic finite-pattern averaging and deterministic integrated-density-of-states results through work of Lenz, Stollmann, Schwarzenberger, and Veselic. Literature on improper-integral averages along uniformly distributed rotation sequences, notably C. Baxa and J. Schoissengeier, **Calculation of improper integrals using `(n alpha)`-sequences**, *Monatshefte fuer Mathematik* 135 (2002), 265--277, DOI `10.1007/s006050200022`, treats precisely the general warning that equidistribution does not automatically control unbounded observables. Alex Furman, **On the multiplicative ergodic theorem for uniquely ergodic systems**, *Annales de l'I.H.P. Probabilites et statistiques* 33:6 (1997), 797--815, is neighboring prior art for the genuinely subadditive Lyapunov boundary that remains open here.

No novelty is claimed for unique ergodicity, syndetic returns, improper-integral averaging, Gram determinants, or Lyapunov exponents. The project-local content is the exact combination forced by the Prime-Circle carrier: PC-254 turns its zero-energy pseudodeterminant into one singular Green-weight average plus two path-run averages, and the rational root-of-unity grids give the explicit tail bound (14), strong enough to make the logarithmic observable uniformly integrable without imposing a Diophantine-rate hypothesis beyond PC-262's rational independence.

The matched-control audit is negative for prime specificity. The proof uses only pairwise coprimality of the three rational partitions, the same Green collision rule, and convergence to the same irrational torus translation. An admissible pairwise-coprime nonprime control sequence with the same limiting `(alpha,beta)` obeys the same strip count, run-frequency limits, and formula (2). Therefore the limiting positive log-volume is not a zeta-specific carrier.

A targeted novelty search around logarithmically singular rotation averages, strictly ergodic finite-range spectral limits, Sturmian/rotation transfer systems, and uniquely ergodic multiplicative cocycles found these established surrounding theories and no missing prime-specific ingredient in (1)--(22). The conclusion does not rely on absence of literature: the reduction is direct.

## 7. Falsification and surviving boundary

The finding has several independent finite/asymptotic checks.

1. A sequence satisfying the PC-262 hypotheses for which the average in (3) does not tend to `(1/2)log(alpha beta)-3` would falsify the tail argument or the conditional-Haar reduction.
2. A collision with `w=0` or nonintegral positive `w` would invalidate the finite lower cutoff (16), contrary to PC-251.
3. Arbitrarily long `p`- or `r`-side collision runs along approximants to one fixed rationally independent `(alpha,beta)` would contradict the robust syndetic visit to the noncollision rectangles (18)--(19).
4. A different asymptotic run-frequency packet for an admissible matched rational-partition control with the same limiting torus data would falsify the source-blind cylinder-frequency reduction.

What survives is now sharper than after PC-262. In the genuinely nonresonant regime, neither the bulk singular histogram nor the zero-energy positive spectral volume can carry source-specific prime information. A surviving mechanism must use a statistic that is both global enough to escape finite-pattern/Haar averaging and not reducible to the determinant of the width-two transfer chain: an extreme/outlier channel, a top Lyapunov or projective-cocycle invariant, a winding/discriminant quantity, a resonance-approach invariant, or another source-forced cross-level construction. Any such candidate still has to beat the matched rational-partition controls and the prior-art boundaries in the Prime-Circle mandate.
