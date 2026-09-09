# PF-253 — the Bessel-four Jacobi chain has a sharp fractional smoothing window

**Status:** `LITERATURE+DERIVED + SHARP-ACTUAL-JACOBI-FRACTIONAL-KERNEL + SHARP-SEPARATED-WINDOW + POSITIVE/ROUTE-NARROWING`.

PF-251 identifies the actual zero-edge branch of each PF-247 parity Jacobi chain, and PF-252 turns that positive branch into an exact weighted nearest-neighbor operator with cubic mass and cubic conductance. The diffusive scaling is radial dimension four, but PF-252 deliberately stops short of a heat-kernel or fractional-functional-calculus theorem.

That missing fixed-axis theorem can be obtained without importing generic first-moment Jacobi scattering. The PF-252 weighted chain satisfies volume doubling and a scale-invariant Poincaré inequality. After adding a fixed lazy holding probability it therefore lies directly in Delmotte's two-sided Gaussian regime for reversible Markov chains. A positive binomial functional-calculus formula then expresses every off-diagonal matrix element of a fractional power as a sum of those Markov kernels with no cancellation.

For every `0<\sigma<1`, this proves the Bessel-four prediction left open in the accepted critical-Jacobi clue. In the separated cone `j>=2i+2`,

\[
\boxed{
\left|\langle e_i,J_\varepsilon^\sigma e_j\rangle\right|
\asymp
(i+1)^{3/2}(j+1)^{-5/2-2\sigma},
}
\tag{1}
\]

uniformly in either parity `\varepsilon`. Consequently, with `Ne_j=(j+1)e_j` and any fixed positive separation `E_d=e^{-dN}`,

\[
\boxed{
E_dJ_\varepsilon^\sigma N^R\in\mathcal S_2
\quad\Longleftrightarrow\quad
0\le R<2+2\sigma,
}
\tag{2}
\]

while for `R>=2+2\sigma` the operator has no bounded extension. In particular, the square-root calibration has the sharp actual-chain threshold `R<3`, improving the free Bessel-three threshold `R<5/2` from PF-249.

This is still a fixed-axis fractional-power theorem, not PF-243's Robin-Poisson theorem. The exact scalar functional factor occurring in the normalized complete-lift source map remains to be derived, and none of the `T_a`, hypercycle, Hardy-end, physical-recoupling, finite-pant, neighboring-module, or global weak-`S_1` gates is discharged here.

## Claim

Fix a parity `\varepsilon\in\{0,1\}` and let `J_\varepsilon` be the corresponding positive half-line Jacobi block from PF-247. Let `\nu=\nu^{(\varepsilon)}` be PF-251's positive zero solution satisfying the actual origin row, and use PF-252's exact ground-state data

\[
m_j=\nu_j^2,
\qquad
c_j=-a_j\nu_j\nu_{j+1}>0,
\tag{3}
\]

so that multiplication by `\nu` is a unitary

\[
U:\ell^2(\mathbb N_0,m)\longrightarrow\ell^2(\mathbb N_0),
\qquad
(Uf)_j=\nu_j f_j,
\tag{4}
\]

and

\[
H:=U^{-1}J_\varepsilon U,
\qquad
(Hf)_j=
\frac{c_j}{m_j}(f_j-f_{j+1})
+\frac{c_{j-1}}{m_j}(f_j-f_{j-1}),
\tag{5}
\]

with `c_{-1}=0`. PF-252 gives

\[
\boxed{
m_j\asymp(j+1)^3,
\qquad
c_j\asymp(j+1)^3,}
\tag{6}
\]

with global comparison constants after absorbing the finite initial segment.

Then for every `0<\sigma<1`:

1. if `q_\sigma(i,j)` is the integral kernel density of `H^\sigma` with respect to `m`, then for `i\ne j`, with `r=|i-j|`,
   \[
   |q_\sigma(i,j)|\lesssim r^{-4-2\sigma};
   \tag{7}
   \]
2. in the separated cone `j>=2i+2`,
   \[
   \boxed{|q_\sigma(i,j)|\asymp |i-j|^{-4-2\sigma};}
   \tag{8}
   \]
3. after conjugating back to counting measure, equation (1) holds;
4. equation (2) is sharp;
5. replacing `N` by the actual parity corridor weight
   \[
   K_\varepsilon e_j=\kappa_{2j+\varepsilon}e_j,
   \qquad
   \kappa_n=n+\alpha,
   \tag{9}
   \]
   changes only constants and the exponential separation rate, not the threshold `R=2+2\sigma`.

The lower bounds in (8) and (1) are important: the threshold in (2) is not only sufficient but genuinely sharp.

## 1. PF-252 gives a uniformly elliptic lazy weighted path

PF-247/PF-252 give `0<=J_\varepsilon<=2`, hence `0<=H<=2`. Put

\[
\eta=\frac14,
\qquad
P:=I-\eta H.
\tag{10}
\]

Writing (5) as a Markov operator gives nearest-neighbor probabilities

\[
P(j,j+1)=\eta\frac{c_j}{m_j},
\qquad
P(j,j-1)=\eta\frac{c_{j-1}}{m_j},
\tag{11}
\]

and holding probability

\[
P(j,j)=1-\eta\frac{c_j+c_{j-1}}{m_j}.
\tag{12}
\]

The diagonal Rayleigh quotient of `H` at vertex `j` is `(c_j+c_{j-1})/m_j<=2`, so

\[
P(j,j)\ge\frac12.
\tag{13}
\]

Thus `P` is a lazy reversible Markov chain. Its symmetric graph weights are

\[
\mu_{j,j+1}=\eta c_j,
\qquad
\mu_{j,j}=m_j-\eta(c_j+c_{j-1}),
\qquad
\sum_k\mu_{jk}=m_j.
\tag{14}
\]

Equation (6) implies uniform two-sided bounds for `c_j/m_j` and `c_j/m_{j+1}`. Together with (13), there is therefore an `a>0` such that every graph neighbor, including the loop, satisfies

\[
\mu_{jk}\ge a\,m_j.
\tag{15}
\]

This is Delmotte's local ellipticity/laziness condition `Delta(a)`.

## 2. The weighted path has dimension-four volume growth and volume doubling

For the graph metric on `\mathbb N_0`, a ball is an interval. From (6), for every `i>=0` and `r>=1`,

\[
V(i,r)
:=\sum_{|j-i|\le r}m_j
\asymp
(r+1)(i+r+1)^3.
\tag{16}
\]

Indeed, when `r` is small compared with `i`, all weights in the ball are comparable to `(i+1)^3`; when the ball reaches the origin, the sum of cubic weights is quartic. In particular,

\[
V(i,2r)\le C V(i,r),
\qquad
V(i,r)\ge c(r+1)^4.
\tag{17}
\]

The quartic lower growth is the discrete counterpart of PF-252's Bessel-four mass law.

## 3. A direct resistance argument proves the scale-invariant Poincaré inequality

Let `I=[L,U]=B(i_0,r)` with `r>=1`. Since the weighted mean minimizes the weighted square error, it is enough to estimate against the endpoint value `f_U`. For `i<U`, Cauchy-Schwarz along the unique path gives

\[
|f_i-f_U|^2
\le
\left(\sum_{\ell=i}^{U-1}\frac1{c_\ell}\right)
\left(\sum_{\ell=i}^{U-1}c_\ell|f_{\ell+1}-f_\ell|^2\right).
\tag{18}
\]

After multiplying by `m_i`, summing in `i`, and reversing the order,

\[
\sum_{i\in I}m_i|f_i-f_U|^2
\le
\sum_{k=L}^{U-1}c_k|f_{k+1}-f_k|^2 A_k,
\tag{19}
\]

where

\[
A_k:=
\sum_{i=L}^{k}m_i
\sum_{\ell=i}^{U-1}\frac1{c_\ell}.
\tag{20}
\]

There is a uniform bound

\[
\boxed{A_k\le Cr^2.}
\tag{21}
\]

If `L>=r`, all indices in `I` are comparable to `L`, so

\[
\sum_{\ell=i}^{U-1}c_\ell^{-1}
\le C(U-i)L^{-3},
\qquad
m_i\le CL^3,
\tag{22}
\]

and summing `U-i` over an interval of length at most `2r` gives (21). If `L<r`, then `U<3r+1`; using the global cubic bounds,

\[
\sum_{\ell=i}^{U-1}c_\ell^{-1}
\le C\sum_{\ell=i}^\infty(\ell+1)^{-3}
\le C(i+1)^{-2},
\tag{23}
\]

so the `i`-th summand in (20) is at most `C(i+1)`, and again (21) follows. Multiplying the edge energy by the fixed `\eta` from (14) only changes the constant.

Hence the weighted graph satisfies Delmotte's Poincaré inequality

\[
\sum_{i\in B(i_0,r)}m_i|f_i-f_B|^2
\le
Cr^2
\sum_{k,\ell\in B(i_0,2r)}
\mu_{k\ell}|f_k-f_\ell|^2.
\tag{24}
\]

For `r<1` the ball contains one vertex and the left side vanishes.

## 4. Delmotte gives two-sided Gaussian bounds

Thierry Delmotte, *Parabolic Harnack inequality and estimates of Markov chains on graphs*, Revista Matemática Iberoamericana 15 (1999), 181--232, DOI `10.4171/RMI/254`, proves that volume doubling, the Poincaré inequality, and the local ellipticity/laziness condition are equivalent to two-sided Gaussian estimates for the reversible Markov chain:

- https://doi.org/10.4171/RMI/254

Equations (15), (17), and (24) verify those hypotheses for the exact PF-252 transformed chain. If `p_k(i,j)=P^k(i,j)` and

\[
h_k(i,j):=\frac{p_k(i,j)}{m_j}
\tag{25}
\]

is the symmetric kernel density with respect to `m`, Delmotte therefore gives constants independent of parity such that, whenever `|i-j|<=k`,

\[
\boxed{
\frac{c}{V(i,\sqrt{k})}
\exp\!\left(-C\frac{|i-j|^2}{k}\right)
\le
h_k(i,j)
\le
\frac{C}{V(i,\sqrt{k})}
\exp\!\left(-c\frac{|i-j|^2}{k}\right).
}
\tag{26}
\]

The constants can be chosen uniformly across the two parity chains because there are only two finite initial coefficient sets and the same asymptotic comparability holds in both.

## 5. Fractional powers are positive sums of the lazy-chain kernels off the diagonal

The loop bound (13) makes

\[
Q:=2P-I
\]

a reversible Markov operator with nonnegative entries. Hence `\sigma(Q)\subset[-1,1]` and `P=(I+Q)/2` has spectrum in `[0,1]`. For `0<\sigma<1`, the absolutely convergent binomial series gives

\[
(I-P)^\sigma
=I-\sum_{k\ge1}\omega_kP^k,
\tag{27}
\]

where

\[
\boxed{
\omega_k
=(-1)^{k+1}{\sigma\choose k}
=
\frac{\sigma\,\Gamma(k-\sigma)}
{\Gamma(1-\sigma)\Gamma(k+1)}
>0,
\qquad
\omega_k\asymp k^{-1-\sigma}.
}
\tag{28}
\]

Since `H=\eta^{-1}(I-P)`, the off-diagonal density of `H^\sigma` is exactly

\[
\boxed{
-q_\sigma(i,j)
=
\eta^{-\sigma}
\sum_{k\ge1}\omega_k h_k(i,j),
\qquad i\ne j.
}
\tag{29}
\]

Every term on the right is nonnegative. The Bessel-four fractional tail is therefore controlled by size estimates alone; no oscillatory cancellation, Jost transfer, or first weighted moment is needed.

## 6. Gaussian summation gives the dimension-four fractional kernel

Let `r=|i-j|>=1`. Since a nearest-neighbor walk cannot cover distance `r` in fewer than `r` steps, (26)--(29), together with `V(i,\sqrt{k})>=ck^2`, give

\[
|q_\sigma(i,j)|
\le
C\sum_{k\ge r}
k^{-3-\sigma}
\exp\!\left(-c\frac{r^2}{k}\right)
\le
Cr^{-4-2\sigma}.
\tag{30}
\]

The last estimate follows by splitting dyadically around `k\asymp r^2`.

For the matching lower bound, assume `j>=2i+2`. Then `r>=i+2`. Restrict (29) to integer times

\[
r^2\le k\le2r^2.
\tag{31}
\]

On this range, (16) gives `V(i,\sqrt{k})<=Cr^4`, the Gaussian exponential in (26) is bounded below by a positive constant, and (28) gives `\omega_k>=cr^{-2-2\sigma}`. There are order `r^2` such times, hence

\[
|q_\sigma(i,j)|
\ge
c\,r^2\cdot r^{-2-2\sigma}\cdot r^{-4}
=
cr^{-4-2\sigma}.
\tag{32}
\]

Combining (30) and (32) proves (7)--(8).

## 7. Conjugation produces the predicted counting-basis exponent

The integral-kernel convention on `\ell^2(m)` is

\[
(H^\sigma f)(i)
=
\sum_j q_\sigma(i,j)f(j)m_j.
\tag{33}
\]

Because `m_j=\nu_j^2`, conjugation by (4) gives

\[
\boxed{
\langle e_i,J_\varepsilon^\sigma e_j\rangle
=\nu_i\nu_j q_\sigma(i,j).
}
\tag{34}
\]

PF-251/PF-252 give `\nu_j\asymp(j+1)^{3/2}`. In the cone `j>=2i+2`, `|i-j|\asymp j+1`, so (8) and (34) yield (1):

\[
|\langle e_i,J_\varepsilon^\sigma e_j\rangle|
\asymp
(i+1)^{3/2}(j+1)^{-5/2-2\sigma}.
\tag{35}
\]

For fixed output `i`, this is precisely the `j^{-5/2-2\sigma}` law predicted but not proved in the previous version of the critical-Jacobi clue. The square-root case is `j^{-7/2}`.

The change from the free PF-250 law `j^{-2-2\sigma}` is exactly the half-power predicted by the shift from Bessel dimension three to four.

## 8. Positive separation gives the sharp full-output threshold

Let

\[
Ne_j=(j+1)e_j,
\qquad
E_d=e^{-dN},
\qquad d>0.
\tag{36}
\]

For `R<2+2\sigma`, split each input sum into `j<2i+2` and `j>=2i+2`. On the near part, boundedness of `J_\varepsilon^\sigma` gives

\[
\sum_{j<2i+2}(j+1)^{2R}
|\langle e_i,J_\varepsilon^\sigma e_j\rangle|^2
\le C_R(i+1)^{2R+1}.
\tag{37}
\]

On the far part, (35) gives

\[
\sum_{j\ge2i+2}(j+1)^{2R}
|\langle e_i,J_\varepsilon^\sigma e_j\rangle|^2
\le
C(i+1)^3
\sum_{j\ge2i+2}(j+1)^{2R-5-4\sigma}.
\tag{38}
\]

The last series converges exactly when

\[
2R-5-4\sigma<-1,
\qquad\text{i.e.}\qquad
R<2+2\sigma.
\tag{39}
\]

Both row bounds grow at most polynomially in `i`, so the exponential factor `e^{-2d(i+1)}` makes the sum over all output rows finite. Thus

\[
E_dJ_\varepsilon^\sigma N^R\in\mathcal S_2
\qquad(R<2+2\sigma).
\tag{40}
\]

For sharpness, take `i=0`. Equation (35) gives

\[
|\langle e_0,J_\varepsilon^\sigma e_j\rangle|
\asymp(j+1)^{-5/2-2\sigma}.
\tag{41}
\]

If `E_dJ_\varepsilon^\sigma N^R` had a bounded extension, its first row would define a bounded functional on `\ell^2`. Its squared tail would therefore have to be summable, but (41) makes it comparable to

\[
\sum_j(j+1)^{2R-5-4\sigma},
\tag{42}
\]

which diverges for `R>=2+2\sigma` and is harmonic at the endpoint. This proves the converse in (2).

Finally `K_\varepsilon\asymp N` and `e^{-dK_\varepsilon}` is bounded above and below, up to constants, by exponentials in `N`. The same proof therefore gives the identical threshold with the actual parity corridor weight in place of `N`.

## 9. Prior-art and novelty audit

Delmotte's volume-doubling/Poincaré characterization and Gaussian bounds for reversible graph walks are classical. Fractional powers, stable-like jump kernels, and subordination/functional-calculus constructions on graphs and metric-measure spaces are also an established literature. No novelty is claimed for any of those general mechanisms.

The closest already-audited discrete half-line fractional-power results remain the free Dirichlet formulas used in PF-248--PF-250, including Gerhat--Krejčiřík--Štampach and Das--de la Fuente-Fernández. Those formulas do not cover the actual PF-247 inverse-square chain. A targeted search likewise found broad stable-like and subordinated-process theory, but not a reason to treat the exponent `4+2\sigma` or the counting-basis exponent `5/2+2\sigma` here as a new general theorem.

The project-specific content is narrower: PF-251/PF-252 supply an exact positive zero mode and cubic weighted path forced by the prime-flute seam geometry; equations (16)--(24) verify the hypotheses of a classical Gaussian theorem for that exact chain; equations (27)--(35) then turn those bounds into the precise fixed-axis fractional matrix decay needed to test the PF-243 smoothing route. The sharp separated threshold in (2) is the corresponding prime-flute source-weight calibration.

No new statement about prime gaps, zeta zeros, or RH follows from this operator estimate alone.

## 10. Consequences and remaining gate

PF-253 resolves one subproblem of the accepted critical-Jacobi clue: **the exact first-moment-critical PF-247 chain does not destroy the free supercritical fractional window.** Its Bessel-four ground-state geometry actually strengthens the literal fractional-power threshold from

\[
R<\frac32+2\sigma
\quad\text{(free Bessel-three)}
\tag{43}
\]

to

\[
\boxed{R<2+2\sigma
\quad\text{(actual Bessel-four chain)}.}
\tag{44}
\]

For a literal square-root edge factor, the fixed-axis chain therefore leaves the large interval `1<R<3` demanded by PF-243.

The next theorem should **not** re-prove generic threshold stability. It should identify the exact scalar function, operator mean, or finite composition of functions of `J_\varepsilon` that enters the seam-normalized far-leg Robin-Poisson factor and determine its leading behavior at `\lambda=0`. Only after that factor is shown to lie in a functional-calculus class controlled by the present estimate should the exponent margin be spent on the `T_a` replacement and the `O(w^2)` hypercycle-coordinate deformation.

## Falsification and audit checks

1. **Ground-state data.** The proof depends on PF-251's positive solution satisfying the actual origin row and PF-252's exact ground-state representation. A tail-only subordinate solution cannot replace it.
2. **Global cubic comparability.** The asymptotics `m_j~C^2j^3`, `c_j~C^2j^3/4` must extend to global two-sided comparability after checking the finite initial segment; positivity makes this immediate but it is part of the theorem's constants.
3. **Laziness.** The fixed choice `eta=1/4` uses `0<=J_\varepsilon<=2` to guarantee `P(j,j)>=1/2`. Without a uniform loop bound, Delmotte's discrete-time lower estimate would need a different treatment.
4. **Poincaré boundary regime.** The case in which a ball reaches the origin must use the summable resistance tail `sum c_j^{-1}\asymp i^{-2}`; treating all weights as locally constant there is invalid.
5. **No cancellation.** Equation (29) relies on `0<\sigma<1`, for which every off-diagonal binomial coefficient has the same sign after extracting the minus sign. The argument does not automatically extend to arbitrary functions of `J`.
6. **Lower cone.** Sharpness uses `j>=2i+2`, where the center is no larger than the diffusion radius at times `k\asymp|i-j|^2`. The global upper bound is broader, but no uniform two-sided claim is made outside this cone.
7. **Actual Robin factor still unknown.** The theorem concerns `J_\varepsilon^\sigma`. It does not identify the complete-lift Robin factor as a positive fractional power or prove PF-243's four separated source-to-bulk estimates.
8. **Later geometry remains open.** `T_a`, Hardy ends, hypercycle reparameterization, physical `P/H` recoupling, finite-pant completion, neighboring-module extension, global weak-`S_1` reassembly, and every RH-level bridge remain outside this finding.