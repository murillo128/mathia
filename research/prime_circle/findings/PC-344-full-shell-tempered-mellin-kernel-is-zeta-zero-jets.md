# PC-344 — full-shell tempered Mellin kernel is exactly zeta-zero jets

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for the tempered-distribution escape left beyond PC-340 and PC-343.

PC-340 closes a broad finite-order non-measure class under an explicit critical-strip admissibility hypothesis, while PC-343 removes every moment hypothesis for arbitrary finite measures once the **full** Prime-Circle shell family is required. The same full-shell rigidity in fact reaches the whole Schwartz-tempered dual. No finite-measure representation, moment condition, compact support, or exponential-moment assumption is needed.

For `n>1`, retain the exact signed-radial Mellin factorization from PC-179,

\[
\mathcal R_n(s)
=-\Gamma(s)\zeta(s)
 n^{1-s}\prod_{p\mid n}(1-p^{s-1})
=:U(s)A_n(s),
\tag{1}
\]

with

\[
A_n(s)=\sum_{d\mid n}\mu(n/d)d^{1-s}.
\tag{2}
\]

Fix `sigma>0`, put `beta=1-sigma`, and let

\[
T\in\mathcal S'(\mathbb R)
\tag{3}
\]

be an arbitrary tempered distribution in the Mellin-frequency variable `t`. Every function `t -> R_n(sigma+it)` belongs to the Schwartz class because Gamma supplies exponential vertical decay, so the full-shell response

\[
L_{\sigma,T}(n)
:=\langle T,\mathcal R_n(\sigma+it)\rangle
\tag{4}
\]

is canonically defined.

Define, with the removable endpoint value understood at `sigma=1,t=0`,

\[
V_\sigma(t):=(\beta-it)U(\sigma+it).
\tag{5}
\]

Then

\[
\boxed{
L_{\sigma,T}(n)=0\quad\forall n>1
\iff
V_\sigma T=0
\quad\text{in }\mathcal S'(\mathbb R).
}
\tag{6}
\]

Consequently:

\[
\boxed{
\begin{aligned}
\sigma\ne1:\quad
&\ker L_\sigma
=\{T\in\mathcal S':V_\sigma T=0\},\\
\sigma=1:\quad
&\ker L_1=\{0\}.
\end{aligned}}
\tag{7}
\]

For `sigma!=1`, the real zeros of `V_sigma` are exactly the ordinates

\[
Z_\sigma:=\{t\in\mathbb R:\zeta(\sigma+it)=0\}.
\tag{8}
\]

If `t_0 in Z_sigma` and the zero `rho=sigma+it_0` of zeta has multiplicity `m_rho`, the local component of any null distribution at `t_0` is exactly

\[
\boxed{
T_{t_0}
=\sum_{k=0}^{m_\rho-1}c_{t_0,k}\,\delta_{t_0}^{(k)}.
}
\tag{9}
\]

Thus the full tempered nullspace consists precisely of tempered, locally finite assemblies of zeta-zero jets whose derivative order is strictly below the corresponding zeta-zero multiplicity. In particular, on a vertical line containing only simple zeta zeros the tempered kernel reduces to tempered discrete measures supported on those ordinates. For `sigma>1` the map is injective.

At the endpoint line `sigma=1`, the pole of zeta is cancelled in (5), `V_1(0)=1`, the classical zero-free theorem gives `zeta(1+it)!=0` for real `t!=0`, and therefore `V_1` has no real zeros at all. Hence no nonzero tempered null distribution survives.

A useful corollary extends PC-343's finite-measure uniqueness statement to the whole tempered class:

\[
\boxed{
L_{1,T}(n)=c\Lambda(n)\quad\forall n>1
\Longrightarrow
T=c\delta_0.
}
\tag{10}
\]

The extra derivative directions at multiple zeta zeros in (9) are not a new spectral mechanism: they are exactly the distributional multiplicity structure of the universal zeta factor already present in (1).

## 1. Full-shell divisor inversion again forces zeros at every integer logarithm

For every integer `m>=2`, ordinary divisor inversion gives

\[
\sum_{\substack{d\mid m\\d>1}}A_d(s)=m^{1-s}-1.
\tag{11}
\]

For complex `z`, set

\[
\Psi_z(t)
:=\int_0^z e^{(\beta-it)w}\,dw
=\frac{e^{(\beta-it)z}-1}{\beta-it},
\tag{12}
\]

where the integral form supplies the removable value when `beta=t=0`, and define

\[
F_T(z):=\langle T,V_\sigma(t)\Psi_z(t)\rangle.
\tag{13}
\]

Whenever `|Im z|<pi/2`, the test function `V_sigma Psi_z` is Schwartz, so (13) is well-defined and holomorphic. At `z=log m`, equations (1), (5), (11), and (12) give exactly

\[
\boxed{
F_T(\log m)
=\sum_{\substack{d\mid m\\d>1}}L_{\sigma,T}(d).
}
\tag{14}
\]

Thus full-shell nulls imply

\[
\boxed{F_T(\log m)=0\qquad(m=2,3,4,\ldots).}
\tag{15}
\]

This is the same all-integer logarithmic zero set that powered PC-343, but the upper growth control now comes directly from the defining seminorms of an arbitrary tempered distribution.

## 2. Tempered continuity still allows only polynomial approach to the Gamma boundary

For every `T in S'(R)` there are constants `C,N` such that

\[
|\langle T,\phi\rangle|
\le
C\sum_{j=0}^{N}
\sup_{t\in\mathbb R}
(1+|t|)^N|\phi^{(j)}(t)|
\qquad(\phi\in\mathcal S).
\tag{16}
\]

For each fixed derivative order `j`, Stirling's formula and standard polynomial vertical-line bounds for zeta and its derivatives give

\[
|V_\sigma^{(j)}(t)|
\le
C_j(1+|t|)^{B_j}e^{-\pi|t|/2}.
\tag{17}
\]

If `|Im z|<=a<pi/2`, differentiating the integral in (12) with respect to `t` yields

\[
|\partial_t^r\Psi_z(t)|
\le
|z|^{r+1}
 e^{|\beta||\operatorname{Re}z|+a|t|}.
\tag{18}
\]

Combining (16)--(18) by Leibniz gives, for some finite constants `C_T,K,M`,

\[
\boxed{
|F_T(z)|
\le
C_T(1+|z|)^M
 e^{|\beta||\operatorname{Re}z|}
\delta^{-K},
\qquad
\delta:=\frac\pi2-a.
}
\tag{19}
\]

The key estimate is elementary:

\[
\sup_{t\in\mathbb R}(1+|t|)^B e^{-\delta|t|}
=O_B(\delta^{-B}).
\tag{20}
\]

Choose an integer `Q` large enough that the zero-free factor

\[
(2\cosh(z/2))^Q
\tag{21}
\]

dominates both the real-direction exponential in (19) and its fixed polynomial factor, and put

\[
H(z):=\frac{F_T(z)}{(2\cosh(z/2))^Q}.
\tag{22}
\]

Then for every `a<pi/2`,

\[
H\in H^\infty(S_a),
\qquad
\boxed{
\log\|H\|_{H^\infty(S_a)}
=O_T\!\left(\log\frac1\delta\right)
}
\tag{23}
\]

as `a` approaches `pi/2`.

So passing from measures to arbitrary tempered distributions enlarges the polynomial exponent in the boundary estimate, but it still cannot change its **polynomial** character.

## 3. The full integer-log zero set still demands essential-exponential boundary growth

Assume `H` is nonzero and choose a real `x_0<0` with `H(x_0)!=0`. Mapping `S_a` to the disk by

\[
\phi_a(z)=\tanh\!\left(\frac{\pi z}{4a}\right),
\qquad
\alpha:=\frac{\pi}{2a}>1,
\tag{24}
\]

sends the zeros `log m` to

\[
\phi_a(\log m)=\frac{m^\alpha-1}{m^\alpha+1}.
\tag{25}
\]

The standard bounded-analytic zero-factor estimate used in PC-343 therefore gives

\[
\log\|H\|_{H^\infty(S_a)}
\ge
\log|H(x_0)|
+2e^{\alpha x_0}\bigl(\zeta(\alpha)-1\bigr).
\tag{26}
\]

As `delta -> 0+`,

\[
\alpha-1\sim\frac{2\delta}{\pi},
\qquad
\zeta(\alpha)\sim\frac1{\alpha-1},
\tag{27}
\]

and hence

\[
\boxed{
\log\|H\|_{H^\infty(S_a)}
\ge
\frac{\pi e^{x_0}+o(1)}{\delta}.
}
\tag{28}
\]

The essential-exponential lower growth in (28) contradicts the logarithmic boundary growth in (23). Therefore

\[
\boxed{F_T\equiv0.}
\tag{29}
\]

No finite-order or polynomially growing singularity allowed by tempered distribution theory can absorb the all-integer zero density generated by the complete shell family.

## 4. Fourier injectivity reduces the entire nullspace to the multiplier kernel

Differentiate (13) on the real axis. Since `V_sigma(t)e^{-itx}` is Schwartz for every real `x`,

\[
0=F_T'(x)
=e^{\beta x}
\langle T,V_\sigma(t)e^{-itx}\rangle.
\tag{30}
\]

Let

\[
S:=V_\sigma T\in\mathcal S'(\mathbb R).
\tag{31}
\]

The function

\[
x\longmapsto\langle T,V_\sigma(t)e^{-itx}\rangle
\tag{32}
\]

is the smooth representative of the Fourier transform of `S`: multiplication by the Schwartz function `V_sigma` regularizes enough that this pairing is well-defined for every `x`, and the distributional Fourier identity follows by testing (32) against an arbitrary Schwartz function of `x`. Equation (30) therefore implies

\[
\widehat S=0,
\qquad
\boxed{V_\sigma T=0.}
\tag{33}
\]

The converse is immediate from (1) and

\[
U(\sigma+it)=\frac{V_\sigma(t)}{\beta-it},
\tag{34}
\]

when `sigma!=1`; at `sigma=1` the same conclusion follows directly from the removable formulation (5) together with (12)--(14). More simply, if `V_sigma T=0`, equation (13) vanishes identically and divisor inversion recovers every shell response. This proves (6).

There is a small endpoint subtlety in that last sentence: equation (14) gives only the divisor sums. Möbius inversion on the divisor poset then gives `L_{sigma,T}(n)=0` for every `n>1`, so no division by `beta-it` is required at `sigma=1`.

## 5. Local distribution theory gives exactly the zeta-zero jets

For `sigma!=1`, the factor `beta-it` is nonzero on the real axis and Gamma has no zeros, so the zero order of `V_sigma` at a real point `t_0` is exactly the multiplicity `m_rho` of the zeta zero `rho=sigma+it_0`.

Equation (33) first implies

\[
\operatorname{supp}T\subseteq Z_\sigma,
\tag{35}
\]

because on any open set where `V_sigma` is nonzero one may divide locally by it. The zero set is discrete. The classical structure theorem for a distribution supported at one point says that the local component of `T` is a finite linear combination of delta derivatives. Multiplication by a function with a zero of order `m_rho` kills precisely

\[
\delta_{t_0},\delta_{t_0}',\ldots,
\delta_{t_0}^{(m_\rho-1)},
\tag{36}
\]

and no higher delta derivative. This proves (9), with the global restriction only that the locally finite jet assembly remain tempered.

At `sigma=1`, `V_1` has no real zero, so (33) implies `T=0` locally at every point and therefore globally. Equation (10) follows by applying the nullspace theorem to `T-c delta_0`, using `R_n(1)=Lambda(n)`.

## 6. Prior-art and novelty audit

The external analytic ingredients are classical: the defining weighted-seminorm estimate for tempered distributions, Stirling decay for Gamma, polynomial vertical-line bounds for zeta and its derivatives, Blaschke/canonical-factor zero estimates on a strip, injectivity of the Fourier transform on `S'`, and the Schwartz structure theorem for distributions supported at a point. Standard distribution references such as Schwartz/Hörmander contain the distributional support and Fourier facts; PC-340 already records neighboring Fourier-Laplace distribution theory, and PC-343 records the Hayman/Blaschke neighborhood used for the strip zero argument.

A directed literature search against tempered-distribution Fourier uniqueness, distributions annihilated by smooth/analytic multipliers, point-supported delta-jet structure, and logarithmic uniqueness sets found the expected classical distribution and Fourier-uniqueness theory, but no independent RH mechanism matching (6)--(9). No historical novelty is claimed for those tools or for the fact that multiplication by a function records the multiplicity of its zeros.

The line-local exact delta is the combination forced by Prime-Circle geometry: **all shell responses create the over-dense set `{log 2, log 3, ...}` while the intrinsic Gamma envelope turns every tempered seminorm into only polynomial boundary blow-up.** This upgrades PC-343 from finite measures to the entire tempered dual and removes the extra admissibility needed by PC-340 because the all-shell zero density is much stronger than the semiprime prime-log density.

No new `SOURCES.md` entry is needed: the proof is explicit, and the external ingredients are the same classical distribution/Blaschke machinery already audited in PC-340 and PC-343 rather than a new load-bearing specialized theorem.

## 7. Consequences and surviving frontier

This closes a natural scalar escape left explicitly open by PC-343. Replacing a finite Mellin measure by an arbitrary tempered distribution does **not** create a new Prime-Circle spectral mechanism. The complete scalar shell family determines every tempered selector modulo nothing except the zero jets of the zeta factor that was already explicit before the selector was introduced.

The multiplicity refinement is exact but tautological from the RH perspective: a simple zeta zero contributes one invisible delta direction, a zero of multiplicity `m` contributes `m` invisible jet directions, and no other tempered null direction exists. This does not explain why zeros occur, why they should lie on `Re(s)=1/2`, or why they should be simple.

The surviving scalar-functional frontier is therefore genuinely beyond tempered distribution theory: Fourier hyperfunctions, ultradistributions, analytic functionals with super-polynomial seminorm growth at the Gamma boundary, or other infinite-order objects. Those classes can support the `exp(c/delta)` boundary growth demanded by the all-integer logarithmic zero set, so the present argument does not classify them. Shell-dependent symbols, nonlinear operations, matrix-valued/noncommuting carriers, and cross-shell/cross-level geometry before scalar Mellin evaluation also remain outside the theorem.

For the canonical research objective, this is a negative result rather than a destination theorem. It sharpens the no-go boundary but supplies neither a new functional equation nor an independent critical-line criterion.

## Audit / falsification tests

A counterexample is a fixed `sigma>0` and `T in S'(R)` such that every shell response (4) vanishes but `V_sigma T!=0`, or, equivalently, a nonzero endpoint-line tempered null selector at `sigma=1`.

The load-bearing checkpoints are:

1. every shell transform and every `V_sigma Psi_z` with `|Im z|<pi/2` must be Schwartz, including the removable endpoint at `sigma=1`;
2. divisor inversion must give exactly (14), hence zeros at every integer logarithm;
3. the general tempered seminorm estimate plus Gamma decay must give only polynomial `delta^{-K}` boundary growth in (19)--(23);
4. the all-integer zero set must force the `zeta(alpha) ~ 1/(alpha-1)` lower bound in (26)--(28), excluding any nonzero `F_T`;
5. the pairing in (32) must indeed represent the Fourier transform of `V_sigma T`, so Fourier injectivity yields (33);
6. local multiplication by a zero of order `m_rho` must kill exactly the delta jets of orders `0,...,m_rho-1` and no higher ones.

Dropping temperedness is a genuine boundary rather than a cosmetic weakening: the proof uses polynomial Schwartz-seminorm control precisely to keep the Gamma-boundary growth below the essential-exponential threshold forced by `{log m}`.