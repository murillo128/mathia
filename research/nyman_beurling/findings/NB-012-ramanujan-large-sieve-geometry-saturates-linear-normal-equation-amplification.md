# NB-012 — Ramanujan large-sieve geometry saturates linear normal-equation amplification

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + RAMANUJAN-DIVISOR-DIAGONALIZATION + LOWER-FRAME-BOUND + METHOD-LEVEL-OBSTRUCTION + PRIME-ENSEMBLE-ASYMPTOTIC-OPTIMALITY`. `NB-011` shows that combining prime-indexed projection equations forces the best Nyman residual to carry truncated semigroup energy of order `d_N^4 log(1/d_N)` by depth polynomial in `d_N^{-1}`. A natural next attempt is to use **all** generator normal equations, including composite indices, in the hope that their extra divisibility patterns amplify the target load by another unbounded factor.

That linear amplification route has a sharp ceiling. Every linear combination of the normal equations admits an exact Ramanujan-sum diagonalization. In the resulting coordinates, its target load is paired only with the von Mangoldt vector, while its harmonic dual energy is controlled by the Euler-totient norm. The exact optimal target-load ratio is

\[
\boxed{
\mathcal R_L
:=\sum_{2\le d\le L}\frac{\Lambda(d)^2}{\varphi(d)}.
}
\tag{1}
\]

Prime powers beyond the first contribute only `O(1)`, so

\[
\boxed{
\mathcal R_L
=\sum_{p\le L}\frac{(\log p)^2}{p-1}+O(1)
=\left(\frac12+o(1)\right)(\log L)^2.
}
\tag{2}
\]

The prime ensemble chosen in `NB-011` attains the prime part of (1) **exactly**. Thus allowing every composite normal equation can change this target-load efficiency only by a bounded additive amount, not by another logarithmic factor.

A second ingredient turns that coefficient statement into a finite-depth method boundary. Ramanujan sums expand into primitive rational frequencies of denominator at most `L`; those frequencies are `L^{-2}`-separated. The Montgomery--Vaughan separated-frequency Hilbert inequality therefore gives a lower frame bound on every sufficiently long block. After dyadic summation,

\[
\boxed{
\sum_{j\le K}\frac{|Q_b(j)|^2}{j}
\ge
c_0\log\!\left(\frac{K}{C_0L^2}\right)
\sum_{d=2}^{L}\varphi(d)|B_d|^2
}
\tag{3}
\]

whenever `K>=C_0L^2`, with absolute constants `c_0,C_0>0`. Here `Q_b` is the divisibility contrast produced by an arbitrary linear combination and `B_d` is its divisor-tail transform, defined below.

Consequently, any proof that follows the `NB-011` interface — form one linear combination of the exact normal equations, treat endpoint/remote terms as errors, and use Cauchy--Schwarz against the harmonic mismatch energy — has target-load efficiency at most

\[
\boxed{
\frac{|T_b|^2}
{\sum_{j\le K}|Q_b(j)|^2/j}
\le
C\,
\frac{\mathcal R_L}
{\log(K/(C_0L^2))}.
}
\tag{4}
\]

At `L\asymp d_N^{-1}` and the `NB-011` cutoff `K\asymp d_N^{-4}` up to logarithmic factors, the right side has order `log(1/d_N)`. Multiplication by the squared target mass `a_N^2=d_N^4` gives the method ceiling

\[
\boxed{O\!\left(d_N^4\log(1/d_N)\right),}
\tag{5}
\]

which matches the lower-bound order already achieved in `NB-011`. **Further linear lower-bound amplification by adding composite normal equations is therefore asymptotically saturated.** This is not an upper bound on the actual semigroup defect and does not obstruct nonlinear use of the equations, a source-specific upper estimate, or a different normed dual certificate.

## 1. Every generator normal equation has one universal divisibility difference

Retain the canonical finite section

\[
V_N=\operatorname{span}\{g_2,\ldots,g_N\},
\qquad
r_N=e-P_{V_N}e,
\qquad
d_N=\|r_N\|,
\qquad a_N=d_N^2,
\]

and Bagchi's harmonic intervals

\[
I_n=\left(\frac1{n+1},\frac1n\right],
\qquad
g_l|_{I_n}=\left\{\frac nl\right\}.
\tag{6}
\]

For any `2<=L<=N`, choose arbitrary complex coefficients `b_l`, `2<=l<=L`, and combine the exact projection equations `\langle r_N,g_l\rangle=0` after multiplying the `l`-th equation by `b_l l`. Put

\[
F_b(n):=
\sum_{l=2}^{L}b_l l\left\{\frac nl\right\}.
\tag{7}
\]

The standard target pairing `\langle e,g_l\rangle=\log l/l` gives the complete target load

\[
\boxed{
T_b:=\sum_{n\ge1}\frac{F_b(n)}{n(n+1)}
=\sum_{l=2}^{L}b_l\log l.
}
\tag{8}
\]

The discrete derivative of each fractional-part coordinate is exact:

\[
l\left(
\left\{\frac jl\right\}
-\left\{\frac{j-1}{l}\right\}
\right)
=1-l\mathbf1_{l\mid j}.
\tag{9}
\]

Hence the coefficient that appears after summation by parts against the mismatch sequence is

\[
\boxed{
Q_b(j)
:=F_b(j)-F_b(j-1)
=\sum_{l=2}^{L}b_l
\left(1-l\mathbf1_{l\mid j}\right).
}
\tag{10}
\]

This is the full analogue of the prime contrast in `NB-011`; no primality has yet been used.

## 2. Ramanujan sums diagonalize the complete divisibility ensemble

For `d>=1`, write the Ramanujan sum

\[
c_d(j)=
\sum_{\substack{1\le a\le d\\(a,d)=1}}
 e^{2\pi i aj/d}.
\tag{11}
\]

The classical finite identity

\[
\sum_{d\mid l}c_d(j)=l\mathbf1_{l\mid j}
\tag{12}
\]

and `c_1(j)=1` turn (9) into

\[
1-l\mathbf1_{l\mid j}
=-\sum_{\substack{d\mid l\\d\ge2}}c_d(j).
\tag{13}
\]

Define the divisor-tail transform

\[
\boxed{
B_d:=\sum_{\substack{l\le L\\d\mid l}}b_l,
\qquad 2\le d\le L.
}
\tag{14}
\]

Then (10) becomes the exact orthogonal-frequency expansion

\[
\boxed{
Q_b(j)=-\sum_{d=2}^{L}B_dc_d(j).
}
\tag{15}
\]

There is no loss of coefficient information. Finite Möbius inversion gives

\[
\boxed{
b_l=
\sum_{k\le L/l}\mu(k)B_{lk},}
\tag{16}
\]

so every vector `(B_2,...,B_L)` is realized by a unique linear combination of the original normal equations.

The target transforms just as cleanly. Since

\[
\log l=\sum_{d\mid l}\Lambda(d),
\tag{17}
\]

substitution into (8) gives

\[
\boxed{
T_b=\sum_{d=2}^{L}\Lambda(d)B_d.
}
\tag{18}
\]

Thus the whole finite family has separated into a target vector `Lambda(d)` and Ramanujan modes `c_d`.

## 3. The exact coefficient optimum is the von-Mangoldt/totient norm

Introduce the Ramanujan coefficient energy

\[
\boxed{
V_b:=\sum_{d=2}^{L}\varphi(d)|B_d|^2.
}
\tag{19}
\]

Cauchy--Schwarz applied to (18) gives

\[
|T_b|^2
\le
\left(
\sum_{d=2}^{L}\frac{\Lambda(d)^2}{\varphi(d)}
\right)
V_b
=\mathcal R_LV_b.
\tag{20}
\]

This constant is **exact**. By (16), the choice

\[
B_d=t\frac{\Lambda(d)}{\varphi(d)}
\tag{21}
\]

for any nonzero scalar `t` comes from an admissible coefficient vector `b`, and equality holds in (20). Therefore

\[
\boxed{
\sup_{b\ne0}\frac{|T_b|^2}{V_b}=\mathcal R_L.
}
\tag{22}
\]

The support of `Lambda` makes the composite boundary transparent. Since `Lambda(d)=0` unless `d=p^a`,

\[
\mathcal R_L
=
\sum_{p\le L}\frac{(\log p)^2}{p-1}
+
\sum_{\substack{p^a\le L\\a\ge2}}
\frac{(\log p)^2}{p^{a-1}(p-1)}.
\tag{23}
\]

The second sum is bounded uniformly in `L`, because its infinite extension equals

\[
\sum_p\frac{(\log p)^2}{(p-1)^2}<\infty.
\tag{24}
\]

The prime number theorem and partial summation then give (2).

Now compare with `NB-011`. Its choice is

\[
b_p=\frac{\log p}{p-1}
\quad(p\le L),
\qquad
b_l=0\quad(l\text{ composite}).
\tag{25}
\]

For this vector, `B_p=b_p` and every composite `B_d` vanishes, so

\[
T_b=V_b=
S_L:=\sum_{p\le L}\frac{(\log p)^2}{p-1}.
\tag{26}
\]

Hence its efficiency is exactly `S_L`, while the unrestricted optimum is `S_L+O(1)`. The prime ensemble is already asymptotically optimal among **all linear combinations** before any finite-depth estimate is imposed.

## 4. Farey spacing gives a uniform lower frame bound for the same modes

The coefficient norm (19) is not merely formal. Expanding (15) with (11) yields

\[
Q_b(j)
=-\sum_{d=2}^{L}
\sum_{\substack{1\le a\le d\\(a,d)=1}}
B_d e^{2\pi i aj/d}.
\tag{27}
\]

All reduced fractions `a/d` appearing here are distinct modulo one. If two have denominators at most `L`, their circular separation is at least `L^{-2}`. The squared coefficient mass of this exponential family is exactly

\[
\sum_{d=2}^{L}\varphi(d)|B_d|^2=V_b.
\tag{28}
\]

Montgomery and Vaughan's generalized Hilbert inequality implies the standard separated-frequency two-sided estimate: there is an absolute constant `C_MV` such that, for every block of `J` consecutive integers,

\[
\boxed{
\sum_{n=M+1}^{M+J}|Q_b(n)|^2
\ge
\left(J-C_{\rm MV}L^2\right)V_b.
}
\tag{29}
\]

The starting point `M` is irrelevant; it only rotates the Fourier coefficients. Equation (29) is the lower-frame counterpart of the familiar large-sieve upper estimate and is useful only once the block length exceeds the Farey-spacing scale.

Choose `J_0>=2C_MV L^2`. On every dyadic block `(J,2J]` with `J>=J_0`, (29) gives at least `(J/2)V_b` unweighted energy, while `1/n>=1/(2J)` on the block. Each such block therefore contributes at least `V_b/4` to the harmonic norm. Summing the dyadic blocks proves that there are absolute constants `c_0,C_0>0` such that

\[
\boxed{
\sum_{j=2}^{K}\frac{|Q_b(j)|^2}{j}
\ge
c_0
\left[\log\!\left(\frac{K}{C_0L^2}\right)\right]_+
V_b.
}
\tag{30}
\]

This is (3). It is uniform in the signs and phases of the normal-equation coefficients and requires no common period of the divisibility patterns.

## 5. The `NB-011` Cauchy interface is saturated in asymptotic order

For the best residual, write as before

\[
\delta_j=c_j(r_N)-a_N.
\tag{31}
\]

When the combined normal equation is split at `K-1`, summation by parts produces the early mismatch functional with coefficients `Q_b(j)` plus one endpoint coefficient, exactly as in `NB-011`. Any use of Cauchy--Schwarz against

\[
\sum_{j\le K}\frac{|\delta_j|^2}{j}
\le\mathcal E_K(r_N)
\tag{32}
\]

must therefore pay a dual norm at least the left side of (30); retaining the endpoint only increases that cost.

Suppose, as in `NB-011`, that the missing finite target tail and the remote residual contribution are controlled as **errors**, so the positive driving term comes from a fixed fraction of the complete target load `a_NT_b`. Even in the idealized zero-error limit, (20) and (30) imply

\[
\frac{a_N^2|T_b|^2}
{\text{harmonic dual cost}}
\le
C a_N^2
\frac{\mathcal R_L}
{\log(K/(C_0L^2))}.
\tag{33}
\]

Endpoint or remote-tail errors cannot improve this bound when they are treated by absolute-value control; they only reduce the usable numerator or increase the denominator.

Take the small-distance regime and the scale used to read `NB-011`,

\[
L\asymp d_N^{-1},
\qquad
K\asymp
\frac{d_N^{-4}}
{\log^4(1/d_N)}
\tag{34}
\]

up to sufficiently large fixed constants. Then

\[
\mathcal R_L\asymp\log^2(1/d_N),
\qquad
\log(K/L^2)\asymp\log(1/d_N),
\tag{35}
\]

and `a_N^2=d_N^4`. Equation (33) becomes precisely (5).

`NB-011` already proves a lower bound `\mathcal E_K(r_N)\gg d_N^4\log(1/d_N)` at an admissible cutoff of this order. Thus the prime construction saturates, up to constants, the strongest asymptotic order available from the entire **linear normal-equation + harmonic Cauchy** architecture.

Using Burnol's `d_N^2\gg1/\log N` only translates the same statement into section size: `L=O(\sqrt{\log N})`, `K=O((\log N)^2)` and the forced energy has order `\log\log N/(\log N)^2`. No improvement of Burnol's distance floor is obtained or claimed.

## 6. Prior art, falsification controls, and research consequence

Ramanujan sums and the identities (12)--(13) are classical; their original systematic treatment goes back to Ramanujan's 1918 paper on trigonometrical sums. The finite lower-frame input is a direct corollary of Montgomery--Vaughan's generalized Hilbert inequality for separated frequencies. The Mathia-specific step is to expose the **complete Nyman normal-equation ensemble** in these coordinates and compare its exact target vector with the harmonic dual norm used by `NB-011`.

A targeted prior-art check covered the core Nyman--Beurling/Báez--Duarte literature already anchored in `SOURCES.md`, searches combining Nyman residuals with Ramanujan sums/divisibility normal equations/large-sieve geometry, and the classical Ramanujan and Montgomery--Vaughan sources. No located Nyman source supplied the transform (14)--(18) in this residual role or the method ceiling (33). Search absence is not a novelty proof; the exact algebra is recorded above and the only quantitative external theorem used in (29) is separately anchored in `SOURCES.md`.

Several boundaries are essential. First, (33) is a **proof-interface ceiling**, not an upper bound for `\mathcal E_K(r_N)`: the actual residual may have much more semigroup energy. Second, it applies when endpoint and remote-tail terms are controlled as errors in the `NB-011` manner. A method that extracts favorable signed information from those terms is not covered. Third, it does not rule out nonlinear combinations of normal equations, higher-order relations among their coefficients, direct target-aware Schur-complement estimates, or a residual-specific upper bound that returns from `\mathcal E_K` to `d_N`. Fourth, prime-power modes can improve finite constants because `\mathcal R_L-S_L` need not vanish; the theorem says only that they cannot change the unbounded asymptotic order.

The durable consequence is therefore negative but directional. `NB-010` showed that one parity equation leaves logarithmic amplification on the table; `NB-011` recovered it with primes. The present result shows that **the remaining composite linear equations cannot recover another asymptotic factor through the same Cauchy mechanism**. The live frontier should now move to the return direction already identified by `NB-011`: derive a source-specific upper estimate on the same truncated semigroup defect, construct a normed dual certificate that uses more than one linear divisibility functional, or exploit signed/nonlinear finite-section structure that lies outside the saturated interface.