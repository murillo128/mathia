# WI-359 — source-norm graph control still cannot make prime thresholds cofinal

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + NON-RH`.

## Claim

`WI-358` proves that the scalar logarithmic-form budget of an actual Suzuki null state is far too weak, by itself, to force autocorrelation continuity across consecutive prime-power thresholds. A natural strengthening is to retain the **operator** zero-mode equation from `WI-257`,

\[
(T_0+K_a)w=0,
\]

and use the resulting graph-norm control

\[
\|T_0w\|_2\le \|K_a\|\,\|w\|_2.
\]

That generic strengthening is still insufficient if the arithmetic perturbation is compressed to a scalar operator-norm envelope.

Let

\[
\Theta(a)=\sum_{n\le e^{2a}}\frac{\Lambda(n)}{\sqrt n},
\qquad
M(a)=\sup_{|u|\le2a}|r''(u)|,
\]

and define the coefficientwise source envelope

\[
\boxed{
U(a):=|\log a|+2\Theta(a)+2aM(a).
}
\tag{1}
\]

For Suzuki's fixed-domain decomposition one has

\[
\boxed{\|K_a\|\le U(a).}
\tag{2}
\]

Nevertheless, if `a_j=(1/2)\log q_j` are consecutive prime-power thresholds as in `WI-358`, there are normalized real smooth vectors

\[
u_j\in C_c^\infty(-1,1)
\]

and bounded self-adjoint rank-at-most-two perturbations `L_j` such that, for all sufficiently large `j`,

\[
\boxed{
(T_0+L_j)u_j=0,
\qquad
\|L_j\|\le U(a_{j+1}),
}
\tag{3}
\]

while the already-active prime-2 autocorrelation still moves by order one between the two threshold scales:

\[
\boxed{
\left|
C_{u_j}\!\left(\frac{\log2}{a_j}\right)
-
C_{u_j}\!\left(\frac{\log2}{a_{j+1}}\right)
\right|
\ge\frac14.
}
\tag{4}
\]

In fact these vectors obey the much stronger graph estimate

\[
\boxed{
\|T_0u_j\|_2=O(a_j),
}
\tag{5}
\]

whereas the source-norm envelope satisfies

\[
U(a)\ge2\Theta(a)=(4+o(1))e^a.
\tag{6}
\]

Thus the consecutive-threshold resolution requires only `O(a)` logarithmic **operator** energy, while the scalar source-norm allowance is exponentially larger.

The consequence is a clean information barrier. The package

\[
\text{common operator domain}
+
\text{zero-mode equation}
+
\text{scalar bound }\|K_a\|\le U(a)
\]

cannot yield a cofinal autocorrelation modulus. Any successful continuation after `WI-358` must use the **specific structure of `K_a`** — its von-Mangoldt weighted translations, the coupling of those channels to one another, the archimedean kernel, firstness, or another source-specific identity — rather than only its boundedness or norm size.

This does not construct a zero mode of Suzuki's actual operator, does not constrain the true first-crossing state, and does not prove or disprove RH. It closes only the norm-compressed operator-equation route.

## 1. Suzuki's arithmetic remainder has an explicit operator-norm envelope

`WI-257`, auditing Suzuki's scaled form, writes on `H=L^2(-1,1)`

\[
\bar q_a=\bar q^0+\bar q_a^1,
\qquad
T_a=T_0+K_a,
\qquad
D(T_a)=D(T_0),
\tag{7}
\]

where `T_0` is the self-adjoint operator associated with the `a`-independent logarithmic principal form and `K_a` is bounded self-adjoint.

Suzuki's equation (4.5), in the normalization already recorded in `WI-357`, gives the bounded part as the scalar `-\log a`, the finite prime-translation sum

\[
-2\sum_{n\le e^{2a}}
\frac{\Lambda(n)}{\sqrt n}
\Re C_w\!\left(\frac{\log n}{a}\right),
\tag{8}
\]

and the continuous-kernel term

\[
-a\int_{-1}^1\int_{-1}^1
r''(a(x-y))w(y)\overline{w(x)}\,dxdy.
\tag{9}
\]

Each compressed translation has operator norm at most one. Hence the operator represented by (8) has norm at most `2\Theta(a)`. For (9), Schur's test gives

\[
\sup_x\int_{-1}^1
 a|r''(a(x-y))|\,dy
\le2aM(a),
\tag{10}
\]

and the same bound in the other variable. Therefore

\[
\|K_a\|
\le|\log a|+2\Theta(a)+2aM(a)=U(a),
\]

which proves (2). This is deliberately a coefficientwise envelope; no cancellation among source channels is retained.

The prime number theorem and partial summation, already used in `WI-358`, give

\[
\Theta(a)=2e^a+o(e^a).
\tag{11}
\]

Since every term in the definition of `U(a)` is nonnegative,

\[
U(a)\ge2\Theta(a)=(4+o(1))e^a.
\tag{12}
\]

The point of (12) is not that the true norm `\|K_a\|` must be this large. It is that any proof which replaces the actual operator by the scalar information (2) has admitted a perturbation class of at least this radius.

## 2. Threshold-scale oscillations cost only `O(a)` in the operator graph norm

Use exactly the consecutive-threshold construction from `WI-358`. Let `q_j<q_{j+1}` be consecutive prime powers,

\[
a_j=\frac12\log q_j,
\qquad
\tau_j=\frac{\log2}{a_j},
\qquad
\delta_j=\tau_j-\tau_{j+1}>0.
\tag{13}
\]

That finding proves

\[
\log\frac1{\delta_j}
\le2a_j+2\log a_j+O(1),
\tag{14}
\]

and constructs a fixed real `\phi\in C_c^\infty(-1/4,1/4)` together with frequencies

\[
Z_j\asymp\delta_j^{-1}
\tag{15}
\]

such that the normalized real modulations

\[
u_j(x)=N_j^{-1}\phi(x)\cos(Z_jx)
\tag{16}
\]

satisfy (4). In particular,

\[
\log(1+Z_j)\le2a_j+2\log a_j+O(1).
\tag{17}
\]

The new point is that these same witnesses are cheap not only for the logarithmic **form** but also for the full principal **operator graph norm**.

On `C_c^\infty(-1,1)`, Suzuki's Fourier identity for the principal form implies that `T_0` is the interval compression of the full-line logarithmic multiplier, up to a fixed scalar. Thus there is a fixed real constant `c_0` such that

\[
\|T_0f\|_{L^2(-1,1)}
\le
\frac1{\sqrt{2\pi}}
\left\| (\log|\xi|+c_0)\widehat f(\xi)\right\|_{L^2(\mathbb R)}
\qquad(f\in C_c^\infty(-1,1)).
\tag{18}
\]

For `f_Z=\phi\cos(Z\cdot)`,

\[
\widehat f_Z(\xi)
=\frac12\bigl(\widehat\phi(\xi-Z)+\widehat\phi(\xi+Z)\bigr).
\tag{19}
\]

Because `\widehat\phi` is Schwartz, a standard shifted-multiplier estimate gives

\[
\boxed{
\left\| (\log|\xi|+c_0)\widehat f_Z(\xi)\right\|_2
\le C_\phi\bigl(1+\log(1+Z)\bigr).
}
\tag{20}
\]

For completeness, split each translated integral into `|\eta|\le Z/2` and `|\eta|>Z/2` after setting `\eta=\xi\mp Z`. On the first region `|\xi|\asymp Z`, so the multiplier is `O(1+\log Z)`. On the second, Schwartz decay dominates both the logarithmic growth at infinity and the locally square-integrable singularity of `\log|\xi|` at zero. The constants are uniform for `Z\ge2`.

Also `N_j\to2^{-1/2}` by Riemann--Lebesgue. Combining (17)--(20) therefore gives

\[
\boxed{
\|T_0u_j\|_2
\le C\bigl(1+\log(1+Z_j)\bigr)
=O(a_j),
}
\tag{21}
\]

which is (5).

So replacing the form budget of `WI-358` by the graph norm of the principal operator does not remove its oscillatory witnesses: consecutive threshold resolution still costs only linear size in `a`.

## 3. The abstract zero-mode equation can be imposed within the same norm allowance

`WI-257` gives an exact rank-at-most-two realization for an arbitrary normalized `u\in D(T_0)`. Put

\[
y=-T_0u,
\qquad
\alpha=\langle y,u\rangle,
\qquad
z=y-\alpha u\perp u,
\tag{22}
\]

and define

\[
Lf
=\alpha\langle f,u\rangle u
 +\langle f,u\rangle z
 +\langle f,z\rangle u.
\tag{23}
\]

Then `L` is bounded self-adjoint, has rank at most two, and

\[
(T_0+L)u=0.
\tag{24}
\]

Moreover,

\[
|\alpha|\le\|T_0u\|_2,
\qquad
\|z\|_2\le\|T_0u\|_2,
\]

so

\[
\boxed{
\|L\|\le3\|T_0u\|_2.
}
\tag{25}
\]

Apply this to `u=u_j`. Equations (21) and (25) give

\[
\|L_j\|=O(a_j).
\tag{26}
\]

But from (12),

\[
U(a_{j+1})\ge(4+o(1))e^{a_{j+1}}.
\tag{27}
\]

Hence, for every sufficiently large `j`,

\[
\|L_j\|\le U(a_{j+1}).
\tag{28}
\]

Together with (4) and (24), this proves (3)--(4).

This stress test is stronger than merely exhibiting vectors inside a graph-norm ball. The witnesses can be made **exact zero modes** of bounded self-adjoint perturbations whose norm lies inside the same scalar source envelope one obtains from Suzuki's actual arithmetic remainder.

## 4. Exact scope of the no-go

The result closes the following proposed continuation of `WI-358`:

1. use the actual null equation only to infer `T_0w=-K_aw`;
2. discard the structure of `K_a` and retain only `\|K_a\|\le U(a)`;
3. derive a graph-norm bound on `w`;
4. hope that this stronger regularity forces old prime autocorrelations to vary by `o(1)` across consecutive source thresholds.

Steps 1--3 are valid, but step 4 is impossible from that information alone. The counterclass (3)--(4) satisfies the same abstract operator-domain and norm constraints while retaining order-one threshold motion.

The scale mismatch is large:

\[
\text{threshold-resolving graph cost}=O(a),
\qquad
\text{coefficientwise source allowance}\ge(4+o(1))e^a.
\tag{29}
\]

Optimizing a generic Fourier split cannot bridge an exponential gap of this kind.

This does **not** show that Suzuki's actual `K_a` admits such a zero mode. The rank-two `L_j` deliberately forgets the arithmetic translation geometry. Therefore the surviving route is exactly the one left open by `WI-257` and `WI-358`: exploit information not invariant under replacement of `K_a` by an arbitrary bounded self-adjoint operator of the same size. Candidate information includes the common von-Mangoldt channel phases, relations among several prime shifts, the signed-source Laplacian constraints of `WI-269`, the distributional support propagation of `WI-267`, or a source-specific coercive reserve.

## 5. Relation to nearby barriers

This finding is not a restatement of the earlier no-go results.

- `WI-248` shows that a **uniform pointwise prime-symbol envelope** has a doubly exponential frequency barrier because prime phases recur. It acts before using a zero-mode equation.
- `WI-249` shows that compact support, odd parity, and density subtraction still allow exponentially large recurrent source discrepancy on arbitrary tests.
- `WI-257` proves that bounded-perturbation zero-modehood gives no qualitative domain upgrade: every vector in `D(T_0)` can be made an abstract zero mode.
- `WI-358` proves that the **scalar form-energy budget** of actual null states does not give cofinal threshold continuity.

The present result fills the remaining gap between `WI-257` and `WI-358`: even the quantitatively stronger **operator graph norm**, together with an exact abstract zero-mode equation and the natural scalar source-norm envelope, still admits the threshold-resolving oscillations. What has to be used next is not more generic regularity but the actual arithmetic shape of the perturbation.

## 6. Prior-art and novelty audit

The literature-backed ingredients are unchanged from the immediately preceding chain.

- Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (17 Aug 2026), supplies the fixed-domain decomposition, the Fourier logarithmic principal form, and the finite translation/continuous-kernel remainder.
- Classical bounded self-adjoint perturbation theory supplies the common operator-domain framework; `WI-257` already audited this against Kato.
- The Prime Number Theorem supplies `\Theta(a)=2e^a+o(e^a)`.
- `WI-358` supplies the exact consecutive-threshold modulation family and the estimate (14).

The Mathia deduction is the quantitative combination (18)--(29): the same threshold-resolving modulations have only `O(a)` **operator** graph cost, and the rank-two realization from `WI-257` fits them inside the exponentially larger scalar perturbation envelope of the actual source.

A targeted audit around Suzuki's localized operator, bounded perturbation graph norms, logarithmic multipliers, and threshold continuity located Suzuki's operator framework and standard perturbation theory but no result formulating this norm-compressed cofinal-threshold obstruction. Search absence is only an audit boundary, not a priority claim.

## Falsification and research disposition

The barrier would fail if any of the following is wrong: the operator envelope (2), the shifted-log-multiplier estimate (20), the threshold-frequency bound inherited from `WI-358`, the rank-two realization/norm estimate (25), or the PNT asymptotic (11). Each step is independent and directly checkable.

Assuming them, do not spend further effort trying to repair `WI-358` by replacing its form-energy budget with a scalar graph-norm or scalar `\|K_a\|` estimate. The next useful theorem must preserve **source coherence** — some invariant of the actual prime translations and archimedean kernel that the rank-two replacement destroys.