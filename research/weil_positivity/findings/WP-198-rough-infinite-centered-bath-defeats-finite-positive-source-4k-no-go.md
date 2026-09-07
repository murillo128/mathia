# WP-198 — A rough infinite centered bath defeats the finite positive-source `4k` no-go

**Status:** `DERIVED + EXACT + HIGHER-ORDER-SPECTRAL-SHIFT + COMMUTING-INFINITE-DIMENSIONAL + SCHATTEN-THRESHOLD + FULL-WEIL-AUTOCORRELATION-CONE + COUNTEREXAMPLE-TO-FINITE-EXTENSION + MATCHED-NONARITHMETIC-CONTROL + DECISIVE-BOUNDARY + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

`WP-196` and `WP-197` show that finite-dimensional monotone-positive pairs cannot use off-zero source spectrum at order `4k`: full positivity on the Weil autocorrelation cone forces the perturbation onto the zero mode. The current `weil_positivity` synthesis therefore leaves infinite-dimensional structure as one of the few honest exits from that classification.

That exit is real, but it has a sharp analytic cost. Let

\[
n=4k,\qquad r=n-1.
\tag{1}
\]

For a bounded commuting positive pair on a separable Hilbert space, the finite zero-mode theorem extends unchanged whenever

\[
V\in\mathcal S^{\,r}=\mathcal S^{\,4k-1}.
\tag{2}
\]

In that class, full order-`4k` Weil-cone positivity still implies `HV=0`.

However the conclusion is false under the natural higher-order spectral-shift hypothesis `V in S^n` alone. For every `n=4k` there is an explicit bounded commuting positive pair

\[
H\ge0,\qquad V\ge0,\qquad
V\in\mathcal S^n\setminus\mathcal S^{n-1},
\qquad HV\ne0,
\tag{3}
\]

whose bare order-`n` Taylor remainder is **strictly positive on every nonzero real smooth compactly supported autocorrelation**.

The mechanism is an infinite source-centered bath with divergent `(n-1)`st source-boundary mass. Its centered spectral-shift Fourier multiplier is bounded below by a positive multiple of `|xi|^{-1/2}` at high frequency, so it can dominate the `O(|xi|^{-1})` oscillation of any fixed off-zero scalar source. This is not an arithmetic bridge: the bath is deliberately hand-engineered and contains no Mangoldt, Gamma, or polar/global data. It is a matched control showing that infinite-dimensional roughness can manufacture the missing cone sign and that the finite-dimensional no-go cannot be extrapolated without a source-variation hypothesis.

## 1. Infinite commuting pairs reduce to an absolutely convergent scalar sum

Let `H=H^*>=0` be bounded and let

\[
0\le V=V^*\in\mathcal S^n,
\qquad [H,V]=0.
\tag{4}
\]

Because `V` is compact, every nonzero eigenspace of `V` is finite-dimensional and reduces `H`. Diagonalizing `H` inside those eigenspaces gives an orthonormal basis of the active subspace with

\[
He_j=c_j e_j,
\qquad
Ve_j=v_j e_j,
\qquad
c_j\ge0,\quad v_j>0,
\tag{5}
\]

while `V=0` on the orthogonal complement.

For an active scalar channel the exact order-`n` density from `WP-194` is

\[
q_j(x)
=
\frac{(c_j+v_j-x)^r}{r!}
\mathbf 1_{[c_j,c_j+v_j]}(x).
\tag{6}
\]

Its mass is

\[
\|q_j\|_1=\frac{v_j^n}{n!}.
\tag{7}
\]

Since `V in S^n`,

\[
\sum_j v_j^n<\infty,
\tag{8}
\]

so

\[
\boxed{
\eta_n(x)=\sum_j q_j(x)
}
\tag{9}
\]

converges in `L^1`. The scalar Taylor remainders are bounded by
`||f^(n)||_infty v_j^n/n!`, so the trace remainder is the absolutely
convergent direct sum and (9) is the canonical `L^1` higher-order
spectral-shift density.

Thus infinite dimension by itself introduces no new matrix mechanism in the commuting category. The only new issue is whether infinitely many source boundaries can change the Fourier tail.

## 2. Summable source variation extends the zero-mode obstruction

Assume now the stronger condition

\[
V\in\mathcal S^{n-1}.
\tag{10}
\]

Each scalar density has distributional derivative

\[
Dq_j
=
J_j\delta_{c_j}-w_j(x)\,dx,
\tag{11}
\]

where

\[
J_j=\frac{v_j^{n-1}}{(n-1)!},
\qquad
w_j(x)
=
\frac{(c_j+v_j-x)^{n-2}}{(n-2)!}
\mathbf 1_{(c_j,c_j+v_j)}(x).
\tag{12}
\]

Moreover

\[
\|w_j\|_1=J_j.
\tag{13}
\]

Hence (10) makes both

\[
\mu:=\sum_j J_j\delta_{c_j}
\tag{14}
\]

a finite positive measure and

\[
w:=\sum_j w_j
\tag{15}
\]

an `L^1` function. Therefore

\[
D\eta_n=\mu-w\,dx.
\tag{16}
\]

With the Fourier convention of `WP-193`,

\[
i\xi\widehat{\eta_n}(\xi)
=
\widehat\mu(\xi)-\widehat w(\xi).
\tag{17}
\]

Riemann--Lebesgue gives `widehat w(xi)->0`. Since the Fourier transform
of the even part is the real part of `widehat eta_n`,

\[
\boxed{
\widehat{\eta_n^{\rm ev}}(\xi)
=
-\frac{S(\xi)}{\xi}
+o(|\xi|^{-1}),
}
\tag{18}
\]

where the uniformly convergent sine series is

\[
S(\xi)
=
\sum_j J_j\sin(c_j\xi).
\tag{19}
\]

Because `sum J_j<infinity`, `S` is a uniform limit of finite
trigonometric polynomials and hence uniformly almost periodic.

If any positive source value carries mass, then `S` is not identically
zero. Indeed, if `S=0`, the odd finite signed measure

\[
\nu
=
\mu-\check\mu,
\qquad
\check\mu(E)=\mu(-E),
\tag{20}
\]

has zero Fourier transform. Uniqueness of Fourier transforms of finite
measures gives `nu=0`; since `mu` is supported on `[0,infinity)`, this
forces `mu((0,infinity))=0`.

A nonzero odd uniformly almost-periodic function has a positive value,
and that value recurs with a fixed positive margin along arbitrarily
large positive arguments. Thus, if `S` is nonzero, there are
`epsilon>0` and `xi_m->infinity` such that

\[
S(\xi_m)\ge\epsilon.
\tag{21}
\]

Equation (18) then yields

\[
\widehat{\eta_n^{\rm ev}}(\xi_m)<0
\tag{22}
\]

for all sufficiently large `m`.

At order `n=4k`, `WP-193` says positivity on every real compactly
supported smooth autocorrelation is equivalent to

\[
\widehat{\eta_n^{\rm ev}}(\xi)\ge0
\qquad(\xi\in\mathbb R).
\tag{23}
\]

Consequently every positive active source must lie at zero:

\[
v_j>0\Longrightarrow c_j=0.
\tag{24}
\]

In the joint eigenbasis this is exactly

\[
\boxed{
H\ge0,\quad V\ge0,\quad [H,V]=0,\quad
V\in\mathcal S^{4k-1}
\quad+\quad
\text{full order-`4k` Weil-cone positivity}
\Longrightarrow
HV=0.
}
\tag{25}
\]

The converse is the infinite direct-sum version of `WP-194`: if
`HV=0`, every active channel is centered, each scalar multiplier is
strictly positive, and the absolutely convergent sum gives

\[
\mathcal R_{4k}(g*\widetilde g;H,V)>0
\tag{26}
\]

for every nonzero real `g in C_c^\infty(R)` whenever `V!=0`.

Thus `WP-196` extends to infinite commuting positive pairs as soon as
the source-boundary jumps have finite total mass.

## 3. The natural `S^n` class can have infinite source-boundary mass

The preceding argument uses one extra Schatten power. That extra power
cannot be removed.

Fix `n=4k` and set

\[
\alpha
=
\frac{2}{2n-1}
=
\frac1{n-\frac12},
\qquad
a_j=j^{-\alpha}.
\tag{27}
\]

Then

\[
\alpha n
=
\frac{2n}{2n-1}>1,
\tag{28}
\]

so

\[
\sum_j a_j^n<\infty.
\tag{29}
\]

But

\[
\alpha(n-1)
=
\frac{2n-2}{2n-1}<1,
\tag{30}
\]

and therefore

\[
\sum_j a_j^{n-1}=\infty.
\tag{31}
\]

Let the **centered bath** be

\[
H_0=0,
\qquad
V_0=\operatorname{diag}(a_1,a_2,\ldots)
\quad\text{on }\ell^2(\mathbb N).
\tag{32}
\]

Then

\[
V_0\in\mathcal S^n\setminus\mathcal S^{n-1}.
\tag{33}
\]

Its spectral-shift density is in `L^1`, but its source value at zero has
infinite `(n-1)`st boundary mass. In particular the bounded-variation
argument of Section 2 is unavailable.

## 4. The centered bath has a slow strictly positive Fourier floor

For a single centered scalar channel of size `a>0`, `WP-194` gives,
for `xi!=0`,

\[
F_a(\xi)
:=
\widehat{\eta_{n,0,a}^{\rm ev}}(\xi)
=
\frac1{(n-3)!\,\xi^2}
\int_0^a
(1-\cos(t\xi))(a-t)^{n-3}\,dt
>0.
\tag{34}
\]

The bath multiplier

\[
F_0(\xi)
=
\sum_{j\ge1}F_{a_j}(\xi)
\tag{35}
\]

converges uniformly because

\[
|F_{a_j}(\xi)|
\le
\|\eta_{n,0,a_j}^{\rm ev}\|_1
=
\frac{a_j^n}{n!}
\tag{36}
\]

and (29) holds. Hence `F_0` is continuous and strictly positive on the
whole real line.

More importantly, it has a quantitative slow tail. If

\[
a|\xi|\ge4,
\tag{37}
\]

then on `0<=t<=a/2`,

\[
(a-t)^{n-3}\ge(a/2)^{n-3},
\tag{38}
\]

while

\[
\int_0^{a/2}(1-\cos(t\xi))\,dt
=
\frac a2-\frac{\sin(a\xi/2)}{\xi}
\ge\frac a4.
\tag{39}
\]

Therefore

\[
\boxed{
F_a(\xi)
\ge
\frac{a^{n-2}}
{2^{\,n-1}(n-3)!\,\xi^2}
\qquad(a|\xi|\ge4).
}
\tag{40}
\]

Let

\[
J(\xi)
=
\left\lfloor
(|\xi|/4)^{1/\alpha}
\right\rfloor.
\tag{41}
\]

For every `j<=J(xi)`, condition (37) holds. Since

\[
p:=\alpha(n-2)<1,
\tag{42}
\]

summing (40) over those indices gives, for sufficiently large `|xi|`,

\[
\begin{aligned}
F_0(\xi)
&\ge
\frac{C_n}{\xi^2}
\sum_{j\le J(\xi)}j^{-p}\\
&\ge
C_n'|\xi|^{-2}
J(\xi)^{1-p}\\
&\ge
C_n''|\xi|^{1/\alpha-n}.
\end{aligned}
\tag{43}
\]

The special choice (27) makes

\[
\frac1\alpha-n=-\frac12.
\tag{44}
\]

Hence

\[
\boxed{
F_0(\xi)\ge C_n''|\xi|^{-1/2}
\qquad(|\xi|\ \text{sufficiently large}).
}
\tag{45}
\]

This slow positive Fourier floor is precisely what finite dimension
cannot provide. It is paid for by the divergence (31).

## 5. One off-zero positive source can be absorbed without losing the cone sign

Now add one scalar off-center channel

\[
H_1=1,
\qquad
V_1=1.
\tag{46}
\]

Let

\[
F_1(\xi)
=
\widehat{\eta_{n,1,1}^{\rm ev}}(\xi).
\tag{47}
\]

The scalar density is

\[
q_1(x)
=
\frac{(2-x)^{n-1}}{(n-1)!}
\mathbf 1_{[1,2]}(x).
\tag{48}
\]

One integration by parts gives

\[
|F_1(\xi)|
\le
|\widehat q_1(\xi)|
\le
\frac{2}{(n-1)!\,|\xi|}
\qquad(\xi\ne0).
\tag{49}
\]

Equations (45) and (49) show that there is `R>0` for which

\[
F_0(\xi)>|F_1(\xi)|
\qquad(|\xi|\ge R).
\tag{50}
\]

On the compact interval `[-R,R]`, continuity and strict positivity give

\[
m_R:=\min_{|\xi|\le R}F_0(\xi)>0,
\qquad
B_R:=\max_{|\xi|\le R}|F_1(\xi)|<\infty.
\tag{51}
\]

Choose an integer

\[
M>\frac{B_R}{m_R}.
\tag{52}
\]

Take `M` orthogonal copies of the centered bath and one copy of the
off-center scalar block:

\[
\mathcal H
=
\bigl(\ell^2(\mathbb N)\otimes\mathbb C^M\bigr)
\oplus\mathbb C,
\tag{53}
\]

\[
H
=
0\oplus 1,
\qquad
V
=
\bigl(V_0\otimes I_M\bigr)\oplus 1.
\tag{54}
\]

Then

\[
H\ge0,\qquad V\ge0,\qquad [H,V]=0,
\tag{55}
\]

\[
V\in\mathcal S^n\setminus\mathcal S^{n-1},
\tag{56}
\]

and

\[
HV\ne0.
\tag{57}
\]

The total even spectral-shift multiplier is

\[
F(\xi)
=
M F_0(\xi)+F_1(\xi).
\tag{58}
\]

By (50)--(52),

\[
\boxed{
F(\xi)>0
\qquad\text{for every }\xi\in\mathbb R.
}
\tag{59}
\]

Applying the exact `WP-193` Fourier criterion at `n=4k` gives

\[
\boxed{
\mathcal R_n(g*\widetilde g;H,V)>0
\qquad
\text{for every nonzero real }
g\in C_c^\infty(\mathbb R),
}
\tag{60}
\]

despite `H>=0`, `V>=0`, and `HV!=0`.

Thus the finite-dimensional theorem does not merely lack a proof in
the natural infinite Schatten class. It is **false** there.

## 6. What is sharp, and what is not

**The `S^{n-1}` threshold is sharp as an ideal-class hypothesis for the commuting argument.**
Section 2 proves zero-mode rigidity throughout `S^{n-1}`, while
Sections 3--5 give a counterexample in `S^n\setminus S^{n-1}`. This
does not assert that every perturbation outside `S^{n-1}` escapes; it
shows that the theorem cannot be extended from `S^{n-1}` to all of
`S^n`.

**The escape is a singular zero-source reservoir, not off-zero geometry becoming positive.**
The extra scalar block still has the oscillatory `O(1/xi)` tail that
kills it in finite dimension. Positivity survives only because the
infinite centered bath has divergent source variation and creates the
slower positive floor (45).

**The construction is deliberately noncanonical.**
The sequence `a_j=j^{-2/(2n-1)}` and the multiplicity `M` are chosen to
win a Fourier domination problem. No Prime Circle, Prime Flute, Prime
Lattice, finite-prime selector, Gamma factor, or polar/global
counterterm forces them. Therefore (60) is a matched control, not
evidence for the primary Weil bridge.

**The control survives removal of all arithmetic data.**
The bath and the off-center block are completely generic operator
spectra. Their positivity cannot distinguish the Riemann source from a
nonarithmetic model.

**Infinite dimensionality is therefore a genuine category change, but
not automatically a useful one.**
A future Mathia construction can no longer be rejected merely because
it has positive off-zero monotone spectrum in infinite dimension. It
must instead show that its critical source singularity or slow Fourier
floor is forced intrinsically and that the same object derives the
finite-prime, archimedean, and global terms.

**Noncommuting infinite pairs remain outside the classification.**
Section 2 uses the compact commuting reduction. `WP-197` closes
noncommutativity only in finite dimension. The present counterexample
already falsifies a universal infinite-dimensional positive-source
no-go inside the commuting subclass, so no stronger noncommuting claim
is needed here.

## 7. Prior art and novelty boundary

The ambient higher-order spectral-shift theory is classical/current
operator theory:

- Denis Potapov, Anna Skripka, and Fedor Sukochev, *Spectral shift
  function of higher order*, Inventiones Mathematicae **193** (2013),
  501--538, DOI `10.1007/s00222-012-0431-2`, proves existence and
  `L^1` control of higher-order spectral-shift functions for Schatten
  perturbations.
- Chandan Pradhan and Anna Skripka, *Positivity of spectral shift
  functions and infinite-dimensional BMV conjecture*, arXiv
  `2512.05587` (2025 preprint), proves nonnegativity of even-order
  spectral-shift functions for Schatten perturbations, including
  infinite-dimensional and possibly unbounded backgrounds.

Those results supply the correct infinite-dimensional operator
category and the independent pointwise sign theorem. They do **not**
identify positivity on the Weil autocorrelation cone, which by
`WP-193` is the different requirement
`widehat(eta_n^ev)>=0`.

The scalar Taylor density, Schatten diagonalization, Fourier
integration by parts, uniqueness of Fourier transforms of finite
measures, and uniform almost periodicity of absolutely convergent
trigonometric series are standard ingredients. The centered truncated
power in (34) is the same Pólya-type positive-definite building block
already classicalized in `WP-194`.

A targeted literature search around higher-order spectral shift,
commuting positive Schatten perturbations, Fourier-positive
spectral-shift densities, positive-definite Taylor remainders, and
Schatten-threshold conditions found the established trace,
integrability, and positivity theory but no theorem matching the
branch-specific pair of statements (25) and (60). Absence of a wording
match is not treated as standalone novelty. The durable Mathia result
is the **exact boundary exposed by the Weil cone**: finite source
variation extends the zero-mode obstruction, while the natural
`S^{4k}` class admits a generic nonarithmetic infinite bath that defeats
it.

## 8. Consequence for `weil_positivity`

The `4k` matched-control laboratory now has a more precise
infinite-dimensional boundary.

Finite monotone-positive geometry is rigid by `WP-197`. Infinite
commuting monotone-positive geometry remains rigid when its source
jumps have finite total `(4k-1)`st mass. But at the natural
higher-order spectral-shift regularity `V in S^{4k}`, a singular
centered reservoir can create enough positive Fourier mass to hide
off-zero source oscillations.

So the surviving question is no longer simply whether an
infinite-dimensional positive completion exists. Generic ones can be
engineered. The source-specific question is whether Mathia forces the
**right** critical infinite reservoir from its own geometry, with a
fixed normalization and no fitted multiplicity, and whether that same
reservoir produces the Mangoldt finite term together with the Gamma
and polar/global sectors before positivity is taken.

This is a stronger control than the finite no-go: any future
infinite-dimensional candidate must now be tested both against
`S^{4k-1}` zero-mode rigidity and against the nonarithmetic bath
construction above. If its sign theorem uses only a slow centered
Fourier floor, that sign is not arithmetically explanatory.

## Dependencies

- `research/weil_positivity/findings/WP-193-higher-order-spectral-shift-positivity-has-a-mod-four-weil-autocorrelation-gate.md`
- `research/weil_positivity/findings/WP-194-source-centered-4k-taylor-remainders-are-weil-cone-positive-and-scalar-centering-is-rigid.md`
- `research/weil_positivity/findings/WP-196-monotone-positive-commuting-backgrounds-force-zero-mode-support-for-4k-weil-cone-positivity.md`
- `research/weil_positivity/findings/WP-197-noncommuting-monotone-positive-finite-backgrounds-still-force-zero-mode-support-at-order-4k.md`

## Bottom line

For commuting positive order-`4k` spectral-shift geometry, finite source
variation preserves the finite-dimensional obstruction:

\[
V\in\mathcal S^{4k-1}
\quad+\quad
\text{full Weil-cone positivity}
\quad\Longrightarrow\quad
HV=0.
\]

But the implication fails in the natural `S^{4k}` class. An explicit
infinite centered bath in
`\mathcal S^{4k}\setminus\mathcal S^{4k-1}` has a strictly positive
Fourier floor of order at least `|xi|^{-1/2}`; enough copies of that
bath absorb the `O(|xi|^{-1})` sign oscillation of a fixed positive
off-zero source. The resulting commuting pair has `H>=0`, `V>=0`,
`HV!=0`, and is nevertheless strictly positive on the full Weil
autocorrelation cone.

Infinite-dimensional roughness is therefore a **real escape from the
finite zero-mode theorem but a completely nonarithmetic one**. Any
Mathia-native use of that escape must derive its critical reservoir and
the finite/archimedean/global arithmetic structure intrinsically,
rather than engineering a Fourier-positive bath.
