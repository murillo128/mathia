# PL-046 — Boas–Kac support rigidity halves the leading localized-Weil prime penalty but remains arithmetic-universal

## Claim

`PL-045` shows that the finite prime-power symbol in a compact Weil window cannot enjoy any **uniform pointwise** cancellation: finite-dimensional Kronecker recurrence drives the prime phases arbitrarily close to complete alignment at arbitrarily large spectral height. There is nevertheless a rigorous non-pointwise gain once one uses the fact that an admissible Weil test is an autocorrelation with compact support.

Let

```text
v in C_c^infinity(-L,L),
f = v * v_tilde,
v_tilde(x)=conjugate(v(-x)).
```

Then `f` is continuous positive definite,

```text
f(0)=||v||_2^2,
supp(f) subset (-2L,2L).
```

For `0<u<2L`, the classical Boas–Kac / Carathéodory–Fejér point-value theorem gives the sharp support-only bound

```text
|f(u)|
  <= c_L(u) f(0),

c_L(u)
  = cos(pi/(ceil(2L/u)+1)).
```

Apply this at the prime-power lags `u=log n`. The non-archimedean part of the localized completed Weil quadratic form is

```text
Q_prime,L(v)
 = -2 sum_(log n<2L) Lambda(n)/sqrt(n) Re f(log n).
```

Therefore

```text
Q_prime,L(v) >= -B_L ||v||_2^2,
```

where

```text
B_L
 = 2 sum_(log n<2L)
       Lambda(n)/sqrt(n)
       cos(pi/(ceil(2L/log n)+1)).
```

The prime number theorem gives the exact leading asymptotic

```text
B_L = (2+o(1)) exp(L).
```

By contrast, the support-blind coefficient-mass envelope used in the pointwise obstruction of `PL-045` is

```text
A_L
 = 2 sum_(log n<2L) Lambda(n)/sqrt(n)
 = (4+o(1)) exp(L).
```

Thus compact-support positive-definiteness removes **one half of the leading worst-case prime penalty** at the level of the aggregate quadratic form. The reason is especially transparent on the dominant outer shell: if

```text
L <= log n < 2L,
```

then `ceil(2L/log n)=2`, so every such lag satisfies

```text
|f(log n)| <= (1/2) f(0).
```

This is a genuine target-relative constraint absent from the bare prime-torus symbol. It also identifies a sharper live operator than the termwise envelope: if `T_u` denotes translation by `u` compressed to `L^2(-L,L)`, then the exact prime penalty is governed by the self-adjoint truncated-shift sum

```text
K_L
 = sum_(log n<2L) Lambda(n)/sqrt(n)
     (T_(log n)+T_(log n)^*),

Q_prime,L(v)=-<v,K_L v>.
```

Hence the best uniform bound is `||K_L||`, and the Boas–Kac estimate proves only

```text
||K_L|| <= B_L = (2+o(1))exp(L).
```

The unresolved non-pointwise question is therefore no longer whether support helps at all — it provably does — but whether the **joint arithmetic geometry of all prime-power lags** forces a substantially smaller norm or another positivity identity than the universal sum of the sharp one-lag bounds.

**Evidence/status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION`. The Boas–Kac / Carathéodory–Fejér extremal theorem is classical prior art, and compactly supported positive-definite factorization is already used explicitly in Weil/trace-formula work of Connes–Consani. The application above is stored as a research-line consequence, not as a novelty claim. It positively exhibits the simplest Paley–Wiener/autocorrelation escape from `PL-045`, while negatively showing that its termwise form is still universal and changes only the leading constant, not the exponential scale of the prime penalty.

## Exact Boas–Kac point-value constraint

For a continuous positive-definite function `f` on `R`, normalized by `f(0)=1` and supported in an interval `(-H,H)`, the classical one-dimensional extremal problem asks for the largest possible `|f(u)|` at a fixed `0<u<H`.

Boas and Kac reduced this to the Carathéodory–Fejér extremal problem. In the modern formulation of Krenedits–Révész, the exact answer is

```text
sup |f(u)|
 = cos(pi/(ceil(H/u)+1)).
```

Taking `H=2L` gives the coefficient `c_L(u)` above.

There is also an operator interpretation which makes the connection with the one-sided geometry of the research line explicit. Define the compressed translation

```text
(T_u v)(x)
  = v(x+u)
```

where both `x` and `x+u` lie in `(-L,L)`, and zero otherwise. Up to the harmless choice of sign convention,

```text
f(u)=<v,T_u v>.
```

If

```text
N=ceil(2L/u),
```

then

```text
T_u^N=0.
```

The sharp numerical-radius bound for this truncated shift is exactly

```text
w(T_u)=cos(pi/(N+1)),
```

which is the same Carathéodory–Fejér constant. Thus the support restriction converts every active prime-power energy `u=log(p^m)` into a **nilpotent one-sided translation** whose numerical radius records how many repeated hops fit inside the Weil window.

For the outer energy shell

```text
L <= u < 2L,
```

one has `N=2`. The corresponding compressed shift squares to zero and has numerical radius `1/2`. This explains the factor `1/2` without invoking any random-phase cancellation.

## Derivation of the asymptotic `B_L ~ 2 e^L`

Put

```text
S(x)=sum_(n<x) Lambda(n)/sqrt(n).
```

Partial summation from the prime number theorem gives

```text
S(x)=(2+o(1))sqrt(x).
```

Split the Boas–Kac envelope into the outer shell and the interior:

```text
B_L
 = 2 sum_(e^L <= n < e^(2L))
       Lambda(n)/sqrt(n) c_L(log n)
   + 2 sum_(n<e^L)
       Lambda(n)/sqrt(n) c_L(log n).
```

On the outer shell, `c_L(log n)=1/2`, hence

```text
B_outer
 = S(e^(2L))-S(e^L)
 = (2+o(1))e^L.
```

For the interior, `0<=c_L<=1`, so

```text
0 <= B_inner
   <= 2 S(e^L)
   = O(e^(L/2)).
```

Therefore

```text
B_L=(2+o(1))e^L.
```

The support-blind mass is instead

```text
A_L=2S(e^(2L))=(4+o(1))e^L.
```

The factor-two gain is therefore an exact asymptotic consequence of compact support plus positive definiteness, not a numerical fit.

## Why this does not contradict `PL-045`

`PL-045` concerns the pointwise trigonometric symbol

```text
P_L(t)
 = sum_(log n<2L)
     2 Lambda(n)/sqrt(n) cos(t log n).
```

Kronecker recurrence proves

```text
limsup_(t->infinity) P_L(t)=A_L.
```

That statement remains untouched. The Boas–Kac inequality does **not** improve the pointwise bound `P_L(t)<=A_L` for every `t`.

The gain appears only after restricting the test object to

```text
f=v*v_tilde,
supp(v) subset (-L,L),
```

and evaluating the *aggregate quadratic form* through the values `f(log n)`. In Fourier language, it uses the global Paley–Wiener coupling among all spectral heights rather than trying to bound the symbol independently at each height.

This distinction is essential. In particular, one cannot simply replace `A_L` by `B_L` inside the pointwise tail threshold of Chuk's one-stroke certificate. A frequency decomposition used in such a pointwise proof need not preserve the compact-support autocorrelation constraint on each piece. The current result supplies a different global bound, not a drop-in improvement of that tail argument.

## The exact joint operator is the sharper surviving target

The termwise Boas–Kac estimate discards compatibility among different lags. Define on `L^2(-L,L)`

```text
K_L
 = sum_(log n<2L) a_n
     (T_(log n)+T_(log n)^*),

a_n=Lambda(n)/sqrt(n).
```

Then `K_L` is finite-rank only after an additional discretization, but it is a bounded self-adjoint finite sum of compressed translations, and

```text
sup_(||v||=1) |Q_prime,L(v)| = ||K_L||.
```

The triangle inequality plus the exact one-lag numerical radii gives

```text
||K_L||
 <= sum_n a_n ||T_(log n)+T_(log n)^*||
 <= B_L.
```

There is no reason for the maximizing vectors of the individual `T_(log n)` to coincide. Consequently `B_L` need not be sharp for the full arithmetic sum.

This isolates a concrete, non-circular research target:

```text
determine the growth and spectral structure of ||K_L||
using the joint set {log(p^m): m log p<2L},
not merely each lag separately.
```

A theorem such as

```text
||K_L|| = o(e^L)
```

or a sign/trace identity coupling the successive prime-power thresholds would be materially stronger than the current universal bound. No such theorem is asserted here.

## Beurling and universality stress test

The one-lag inequality is **not arithmetic-specific**. If a generalized prime system, or any positive discrete frequency measure, replaces the rational-prime energies by positive lags `omega_j`, then every autocorrelation supported in `(-2L,2L)` satisfies the identical bound

```text
|f(omega_j)|
 <= cos(pi/(ceil(2L/omega_j)+1)) f(0).
```

Thus the mechanism survives arbitrary deformation of the energy set. Only the counting asymptotic used to turn the weighted sum into the specific constant `(2+o(1))e^L` knows the ordinary prime number theorem.

Accordingly, the factor-two improvement is **support rigidity**, not Riemann-zero rigidity. A successful next step must exploit joint relations among the exact rational-prime lags, a zeta-specific global observable, or the completed archimedean coupling in a way that fails for matched generalized-frequency controls.

## Analytic-continuation boundary

No Euler product is continued into the critical strip.

The arithmetic term comes from the completed Weil explicit formula, where analytic continuation and the archimedean contribution are already part of the established identity. For each fixed `L` the von-Mangoldt sum is finite. The Boas–Kac estimate is a theorem about positive-definite compactly supported functions on the real line, and the asymptotic uses only the prime number theorem.

Therefore the result survives the analytic-continuation audit cleanly.

## Prior-art and novelty audit

The relevant ingredients are classical or established:

- **R. P. Boas Jr., M. Kac**, “Inequalities for Fourier transforms of positive functions,” *Duke Mathematical Journal* **12** (1945), 189–206. Classical source of the compact-support positive-definite point-value extremal theorem.
- **Sándor Krenedits, Szilárd Gy. Révész**, “The point value maximization problem for positive definite functions supported in a given subset of a locally compact group,” *Proceedings of the Edinburgh Mathematical Society* **61**(1) (2018), 179–200, DOI `10.1017/S0013091517000062`, arXiv:`1504.03808`. Its review of the Boas–Kac theorem states explicitly that for `(-H,H) subset R` the sharp normalized value at `u` is `cos(pi/(ceil(H/u)+1))`.
- **Alain Connes, Caterina Consani**, “Weil positivity and trace formula, the archimedean place,” *Selecta Mathematica* **27**(4) (2021), Paper 77, DOI `10.1007/s00029-021-00689-4`, arXiv:`2006.13771`. Proposition 3.2 explicitly imports the Boas–Kac compact-support convolution-square theorem into a Weil/trace-formula setting, so the positive-definite support bridge itself is direct prior art in this area.
- **Marcus Chuk**, “Weil positivity in compact windows: certified two-sided bounds and a Landau–Widom decay law,” arXiv:`2608.24827` (submitted 25 August 2026), preprint. `PL-045` records its sharp pointwise prime-comb envelope and the resulting doubly exponential barrier for that particular certificate.

A targeted search for the combination of the exact Boas–Kac point-value constant with Chuk's localized prime-comb bound did not identify a stronger published theorem that would make the aggregate estimate above obsolete. That absence is **not** treated as evidence of novelty. The stored contribution is the audited consequence and its boundary: the simplest support-aware non-pointwise mechanism really improves the arithmetic envelope, but the improvement is universal, termwise, and leaves the genuinely joint prime-lag operator norm unresolved.

## Consequence for the research line

The compact-window picture can now be sharpened to

```text
bare prime symbol at fixed spectral height
    -> Kronecker recurrence restores full amplitude A_L~4e^L
       arbitrarily far out                              [PL-045]

admissible Weil autocorrelation with support (-2L,2L)
    -> each prime-power lag is a nilpotent truncated shift
    -> exact Boas-Kac numerical-radius constraint
    -> aggregate universal envelope B_L~2e^L           [PL-046]

joint rational-prime truncated-shift family
    -> exact penalty ||K_L|| <= B_L
    -> possible additional cancellation/rigidity is not classified.
```

Thus the next useful investigation is not another appeal to generic phase cancellation and not another independent-lag inequality. It is the **joint spectral geometry of the compressed prime-power translations**, or an equally strong target-relative identity, tested against Beurling/generalized-frequency controls. That is the first remaining place in this compact-Weil branch where arithmetic interactions among many exact `log p` directions could still contribute information beyond universal support theory.