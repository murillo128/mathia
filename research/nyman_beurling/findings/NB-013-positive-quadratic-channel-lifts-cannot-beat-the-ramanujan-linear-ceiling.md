# NB-013 — positive quadratic channel lifts cannot beat the Ramanujan linear ceiling

**Status:** `EXACT-DERIVED + MULTICHANNEL-PSD + LOEWNER-DOMINATION + DIMENSION-FREE-METHOD-OBSTRUCTION + LINEAR-CEILING-STABILITY`. `NB-012` shows that one arbitrary linear combination of the finite Nyman normal equations has target-load efficiency controlled by the Ramanujan coefficient norm

\[
\mathcal R_L=\sum_{2\le d\le L}\frac{\Lambda(d)^2}{\varphi(d)}
=\left(\frac12+o(1)\right)(\log L)^2,
\]

and that the prime combination of `NB-011` already attains the leading order. A natural next escape is to keep **many** normal-equation channels simultaneously and combine their squared outputs, cross terms, or an arbitrary positive-semidefinite channel form, hoping that coherent multichannel aggregation buys an additional factor that no single linear combination can see.

It cannot. The scalar Ramanujan coefficient inequality and the separated-frequency lower frame bound of `NB-012` polarize to matrix inequalities. For every finite family of normal-equation channels, of arbitrary cardinality and with arbitrary complex coefficients, the target channel is rank one and satisfies a dimension-free Loewner domination by the harmonic channel Gram matrix. Consequently every positive-semidefinite quadratic combination has the same maximal target-load efficiency as the one-channel Rayleigh quotient, up to the same separated-frequency logarithmic factor.

More precisely, if all channels use generators of index at most `L` and the common harmonic cutoff `K` is beyond the Farey-spacing scale, then

\[
\boxed{
 tt^*\preceq
 \frac{\mathcal R_L}
 {c_0\log(K/(C_0L^2))}\,H_K,
}
\tag{1}
\]

with the constants `c_0,C_0` from `NB-012`. Here `t` is the vector of complete target loads and `H_K` is the channel Gram matrix in the harmonic mismatch norm. Equivalently,

\[
\boxed{
 t^*H_K^+t
 \le
 \frac{\mathcal R_L}
 {c_0\log(K/(C_0L^2))},
}
\tag{2}
\]

and for every positive-semidefinite channel matrix `W`,

\[
\boxed{
 t^*Wt
 \le
 \frac{\mathcal R_L}
 {c_0\log(K/(C_0L^2))}
 \operatorname{tr}(WH_K).
}
\tag{3}
\]

Thus channel count, redundant equations, coherent positive cross-channel mixing, and residual-dependent choice of the channel family cannot improve the asymptotic order available from the `NB-011`/`NB-012` lower-bound interface. At `L\asymp d_N^{-1}` and the admissible `NB-011` scale `K\asymp d_N^{-4}` up to logarithmic factors, every such positive quadratic lift remains capped at

\[
\boxed{O\!\left(d_N^4\log(1/d_N)\right),}
\tag{4}
\]

matching the order already forced by `NB-011`. The next useful conversion mechanism must therefore leave the positive quadratic closure of the finite normal equations, use a source-specific upper estimate, or introduce genuinely different target-relative structure.

## 1. The complete coefficient geometry is already a Hilbert space

Retain the notation of `NB-012`. An arbitrary linear combination of the normal equations up to generator depth `L` is represented after divisor-tail inversion by coefficients

\[
B=(B_d)_{2\le d\le L},
\]

with target load

\[
T(B)=\sum_{d=2}^{L}\Lambda(d)B_d
\tag{5}
\]

and Ramanujan coefficient norm

\[
\|B\|_V^2
:=\sum_{d=2}^{L}\varphi(d)|B_d|^2.
\tag{6}
\]

The exact coefficient optimum proved in `NB-012` is simply the norm of the target functional on this finite Hilbert space:

\[
\boxed{
|T(B)|^2\le\mathcal R_L\|B\|_V^2,
\qquad
\mathcal R_L
=\sum_{d=2}^{L}\frac{\Lambda(d)^2}{\varphi(d)}.
}
\tag{7}
\]

Equality is attained by `B_d` proportional to `Lambda(d)/phi(d)`. This is already a statement about the **whole coefficient space**, not only about a preferred scalar channel.

Choose now any finite channel family

\[
B^{(1)},\ldots,B^{(r)},
\tag{8}
\]

where `r` may grow with `L` or with the Nyman section. Define the coefficient Gram matrix and target vector by

\[
V_{\alpha\beta}
:=\sum_{d=2}^{L}\varphi(d)
 B_d^{(\alpha)}\overline{B_d^{(\beta)}},
\qquad
 t_\alpha:=T(B^{(\alpha)}).
\tag{9}
\]

For every `x in C^r`, applying (7) to `sum_alpha x_alpha B^(alpha)` gives

\[
|x^*t|^2\le\mathcal R_L\,x^*Vx.
\]

Therefore the scalar coefficient inequality is exactly equivalent to the matrix domination

\[
\boxed{tt^*\preceq\mathcal R_L V.}
\tag{10}
\]

No independence of the channels is required. If the family is redundant, both sides simply have the corresponding null directions.

## 2. The separated-frequency lower frame bound also polarizes

For each channel let

\[
Q_\alpha(j)
=-\sum_{d=2}^{L}B_d^{(\alpha)}c_d(j)
\tag{11}
\]

be its Ramanujan divisibility contrast, and define the harmonic channel Gram matrix

\[
(H_K)_{\alpha\beta}
:=\sum_{j=2}^{K}
\frac{Q_\alpha(j)\overline{Q_\beta(j)}}j.
\tag{12}
\]

`NB-012` proves that there are absolute constants `c_0,C_0>0` such that every scalar coefficient vector `B` obeys

\[
\sum_{j=2}^{K}\frac{|Q_B(j)|^2}{j}
\ge
c_0
\left[\log\!\left(\frac{K}{C_0L^2}\right)\right]_+
\|B\|_V^2.
\tag{13}
\]

Apply (13) to every channel combination `sum_alpha x_alpha B^(alpha)`. Writing

\[
\lambda_{K,L}
:=c_0\left[\log\!\left(\frac{K}{C_0L^2}\right)\right]_+,
\tag{14}
\]

we obtain for every `x`

\[
x^*H_Kx\ge\lambda_{K,L}x^*Vx.
\]

Hence

\[
\boxed{H_K\succeq\lambda_{K,L}V.}
\tag{15}
\]

This matrix statement is not an additional large-sieve theorem. It is the polarization of the scalar lower frame bound already proved in `NB-012`. Its importance here is that it keeps all cross-channel interference exactly rather than estimating channels one at a time.

When `lambda_(K,L)>0`, combining (10) and (15) gives

\[
tt^*
\preceq\mathcal R_LV
\preceq\frac{\mathcal R_L}{\lambda_{K,L}}H_K,
\]

which is (1).

## 3. Every positive quadratic channel form inherits the same ceiling

Let `W` be any positive-semidefinite `r x r` matrix. Taking the trace after multiplying the Loewner inequality (1) by `W` gives

\[
\operatorname{tr}(Wtt^*)
\le
\frac{\mathcal R_L}{\lambda_{K,L}}
\operatorname{tr}(WH_K).
\]

Since `tr(Wtt*)=t*Wt`, this is (3). Thus no choice of positive channel weights or positive cross-channel coherences can produce a target quadratic form whose ratio to its harmonic dual cost exceeds the one-channel coefficient ceiling.

There is a coordinate-free equivalent. The Loewner relation

\[
tt^*\preceq C H_K
\tag{16}
\]

holds if and only if `t` lies in the range of `H_K` and

\[
t^*H_K^+t\le C.
\tag{17}
\]

Using `C=R_L/lambda_(K,L)` gives (2). The quantity on the left is exactly the strongest least-energy extraction obtainable when **all retained channel constraints are solved jointly** rather than collapsed first to one scalar combination. Thus the absence of a channel-count gain is not an artifact of using traces in (3).

This also makes the basis invariance explicit. Replacing the channel family by any invertible linear recombination sends `(t,H_K)` to the corresponding congruent pair and leaves `t*H_K^+t` unchanged. Adding redundant channels changes neither the represented constraint space nor its optimal efficiency.

## 4. Splicing the matrix ceiling into the actual residual architecture

For the best residual write, as before,

\[
a_N=d_N^2,
\qquad
\delta_j=c_j(r_N)-a_N,
\qquad
T_K(r_N)=\sum_{j=2}^{K}\frac{|\delta_j|^2}{j}
\le\mathcal E_K(r_N).
\tag{18}
\]

Each channel normal equation, after truncation and summation by parts, evaluates a linear functional of the mismatch vector whose representer is `Q_alpha(j)` together with the single endpoint coefficient recorded in `NB-011`--`NB-012`. If the complete target tail and remote residual tail were absent, the channel-output vector would be exactly `-a_N t`. The smallest harmonic mismatch energy compatible with all those exact channel outputs would then be

\[
a_N^2 t^*H_K^+t.
\tag{19}
\]

Equation (2) shows that even this **ideal zero-error multichannel problem** can force at most

\[
\boxed{
 a_N^2\frac{\mathcal R_L}{\lambda_{K,L}}.
}
\tag{20}
\]

The actual finite equations contain the endpoint and remote-tail terms already tracked in `NB-011`. Folding the endpoint coordinate into the channel Gram matrix only adds a positive-semidefinite matrix to `H_K`, which can only decrease the generalized target efficiency. Treating the missing target tail and remote residual term by absolute-value error bounds, as in the existing architecture, reduces the usable driving vector rather than creating a new positive target channel. Therefore those terms cannot invalidate the ceiling (20) for this method class.

At the `NB-011` small-distance scales

\[
L\asymp d_N^{-1},
\qquad
K\asymp
\frac{d_N^{-4}}{\log^4(1/d_N)}
\tag{21}
\]

up to sufficiently large constants, `NB-012` gives

\[
\mathcal R_L\asymp\log^2(1/d_N),
\qquad
\lambda_{K,L}\asymp\log(1/d_N).
\tag{22}
\]

Since `a_N^2=d_N^4`, equation (20) becomes (4). `NB-011` already achieves the matching lower-bound order. Hence arbitrary positive quadratic multichannel use of the same finite normal equations does not reopen the linear amplification route.

## 5. Adversarial controls and exact scope

Several distinctions are load-bearing.

First, positivity of the channel form is essential. An indefinite quadratic expression is not ordered by Loewner domination and may exploit cancellation between channel energies. It also ceases to be an automatic nonnegative lower-bound certificate; any such use needs a separate source theorem controlling its sign. This finding does not rule it out.

Second, the result concerns a common generator depth `L` and a common harmonic cutoff `K`. Channels using different depths can be embedded into their maximum depth, but genuinely multiscale observables that couple different cutoffs before taking a positive form require their own bookkeeping. No claim is made that every nonlinear finite-section argument reduces to (3).

Third, the channel family may be arbitrarily large, linearly dependent, or selected after `N`, `d_N`, and the available source data are known. Equations (10) and (15) hold pointwise for every chosen family, so adaptive selection does not create a dimension factor. What is excluded is only gain from **positive quadratic closure of the same linear normal-equation information**.

Fourth, the method ceiling is not an upper bound on the actual semigroup defect `E_K(r_N)`. The residual may contain substantially more energy than `NB-011` forces. A source-specific upper estimate for that energy, a nonlinear relation among residual coordinates, or a target-aware dual certificate in another norm remains outside the obstruction and could still change the approximation problem.

Finally, the argument does not improve or rederive Burnol's distance bound and makes no RH implication. Translating (4) into section size still uses the same known lower scale for `d_N` as `NB-011`--`NB-012`.

## 6. Prior-art boundary and research consequence

The only load-bearing analytic inputs are already canonical in `NB-012`: Ramanujan's divisor-frequency decomposition and the Montgomery--Vaughan separated-frequency Hilbert inequality, both anchored in `SOURCES.md`. The passage from their scalar inequalities to (10), (15), and the pseudoinverse form (2) is standard finite-dimensional Hilbert/Loewner geometry; no new external theorem is imported.

A targeted literature search over Nyman--Beurling finite sections, Ramanujan-sum normal equations, residual Gram methods, and positive quadratic/multichannel variants located general Nyman polynomial-approximation work but no source using this Ramanujan normal-equation channel geometry to obtain a multichannel positive-semidefinite amplification beyond the scalar large-sieve interface. Search absence is not a novelty claim. Since no additional specialized literature result is load-bearing, `SOURCES.md` remains unchanged.

The durable frontier is therefore narrower than `NB-012` alone states. It is not enough to replace one optimized normal-equation combination by a bank of channels, retain all cross terms, and square them positively: the target remains a rank-one functional inside the same coefficient Hilbert space, and the same Ramanujan/Farey frame controls the entire bank at once. To improve the finite transport from residual structure to `d_N`, the next mechanism must use information not represented by this positive quadratic closure—for example a sign-indefinite source observable with an independently justified sign, a genuinely nonlinear residual identity, a multiscale coupling outside one common cutoff, or an upper estimate that can squeeze the already-forced early defect.