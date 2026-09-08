# XF-108 — mass-preserving prime deposition PNT-cancels smooth q-scale Toeplitz witnesses

**Status:** `EXACT-DERIVED` + `INTERFACE-NORMALIZATION` + `PNT-CANCELLATION` + `TOEPLITZ-ROUGHNESS-GATE`. XF-106 and XF-107 forced any negative source-Toeplitz witness at the natural arithmetic scale to be both collective and long-range. There is a further obstruction to the obvious continuum route. Once the prime-power atoms are deposited on the mesh with exact mass preservation, the prime number theorem cancels the leading archimedean `e^xi` background against every Toeplitz test direction whose lag autocorrelation remains physically smooth. The q-scale continuum quadratic form is therefore asymptotically the identity, not the unstable integral operator suggested by the archimedean term alone.

Keep the source scales

\[
N=2q^2,\qquad
\Delta^2\asymp q^{-3},\qquad
a:=N\Delta\asymp q^{1/2},
\tag{1}
\]

so in particular

\[
\Delta\asymp a^{-3}.
\tag{2}
\]

Fix

\[
L=\log a+c,\qquad
K=\left\lfloor\frac{L}{\Delta}\right\rfloor,
\qquad c\in\mathbf R \text{ fixed}.
\tag{3}
\]

The conclusion is that a negative Toeplitz witness cannot have a bounded, or even mildly growing, physical Lipschitz constant in lag. Quantitatively, there is `c_1>0` depending only on the classical prime-number-theorem error constant and on the fixed deposition bump such that every unit vector producing a nonpositive quadratic form must satisfy, for all sufficiently large scales,

\[
\boxed{
1+\max_{1\le m<K}
\frac{|r_{m+1}-r_m|}{\Delta}
\ge
\exp\!\bigl(c_1\sqrt{\log a}\bigr),
}
\tag{4}
\]

where

\[
r_m=\sum_{j=0}^{K-m}v_jv_{j+m}.
\tag{5}
\]

Thus the source-side obstruction isolated by XF-107 must be **collective, q-scale in span, and increasingly rough in its lag autocorrelation**. A smooth q-scale continuum eigenfunction cannot provide the missing negative Toeplitz direction.

## 1. Normalize prime deposition by mass, not by mesh phase

XF-102 used a fixed nonnegative smooth bump `psi`, supported in `[-1,1]` and positive on `[-1/2,1/2]`, to deposit each prime-power atom near its logarithmic frequency

\[
\lambda_n=\frac12\log n.
\tag{6}
\]

For q-scale Toeplitz tests there is a normalization issue that was harmless in the earlier fixed-`ell^1` estimates but becomes leading-order here. Define the positive periodic denominator

\[
p_\psi(u)
=
\sum_{j\in\mathbf Z}\psi(j-u).
\tag{7}
\]

The nearest integer to `u` lies within `1/2`, so the hypotheses on `psi` give constants

\[
0<c_\psi\le p_\psi(u)\le C_\psi<\infty
\qquad (u\in\mathbf R).
\tag{8}
\]

Deposit an atom with the normalized weights

\[
\omega_\psi(m,u)
=
\frac{\psi(m-u)}{p_\psi(u)}.
\tag{9}
\]

They retain exactly the same one-mesh-cell localization as XF-102, but now satisfy

\[
\boxed{
\sum_{m\in\mathbf Z}\omega_\psi(m,u)=1
}
\tag{10}
\]

for every phase `u`. Because a smooth compactly supported bump vanishes at the support endpoints, at an integer mesh phase one also has the cardinal property

\[
\omega_\psi(m,j)=\mathbf 1_{m=j}.
\tag{11}
\]

Replace the source moments of XF-102 by the mass-preserving variant

\[
\widehat Q_m^\psi
=
B(m\Delta)
-
\frac1{2\Delta}
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}\,
\omega_\psi\!\left(m,\frac{\lambda_n}{\Delta}\right),
\qquad
1\le m\le K,
\tag{12}
\]

where XF-052 gives

\[
B(\xi)
=
e^\xi-\frac{e^{-5\xi}}{1-e^{-4\xi}}.
\tag{13}
\]

This normalization does not change the scale bookkeeping of XF-102--XF-107. The denominator in `(9)` is bounded above and below by fixed constants, the support is unchanged, and the nearest mesh point still receives a fixed positive fraction of each atom. Therefore the prime visibility, Chebyshev mass bounds, the XF-105 untouched-cell lower bound, and the XF-106/XF-107 local Toeplitz estimates survive with constants depending on `psi`.

What changes is the continuum meaning: every prime-power atom now contributes exactly its intended total mass, independently of its fractional phase relative to the mesh.

## 2. The Toeplitz quadratic form is a smooth logarithmic prime test

Normalize

\[
\widehat\mu_0=1,\qquad
\widehat\mu_m=\frac{\widehat Q_m^\psi}{N},
\qquad
\widehat\mu_{-m}=\widehat\mu_m,
\tag{14}
\]

and let

\[
\widehat T_K
=
(\widehat\mu_{i-j})_{0\le i,j\le K}.
\tag{15}
\]

The matrix is real symmetric, so a lowest-eigenvalue witness can be chosen real. For a real unit vector

\[
v=(v_0,\ldots,v_K),\qquad \|v\|_2=1,
\tag{16}
\]

define its lag autocorrelation by `(5)`. Then `|r_m|\le1` and

\[
v^\top\widehat T_Kv
=
1+2\sum_{m=1}^K\widehat\mu_m r_m.
\tag{17}
\]

The mass-normalized deposition defines an interpolation of these lags,

\[
R_v(\xi)
=
\sum_{m\in\mathbf Z}
\omega_\psi\!\left(m,\frac{\xi}{\Delta}\right)r_m,
\tag{18}
\]

with `r_m=0` outside the visible range when needed. Away from the two endpoint mesh cells, `(10)` and `(11)` imply

\[
R_v(m\Delta)=r_m.
\tag{19}
\]

Set

\[
\mathcal L(v)
:=
1+
\max_{1\le m<K}
\frac{|r_{m+1}-r_m|}{\Delta}.
\tag{20}
\]

On each interior mesh interval, constant reproduction in `(10)` makes the derivative depend only on adjacent differences, not on the absolute size of `r_m`. Consequently

\[
\|R_v\|_\infty\le1,
\qquad
\|R_v'\|_\infty
\ll_\psi \mathcal L(v)
\tag{21}
\]

away from endpoint strips of width `O(Delta)`.

With `r_m=0` outside the visible range, the prime part of `(17)` is exactly the logarithmic von-Mangoldt test

\[
-\frac1a
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}\,
R_v(\lambda_n).
\tag{22}
\]

The only loss at the endpoints appears when this test is compared with a smooth Stieltjes integral. The upper taper has logarithmic width `O(Delta)`; it corresponds to `O(Delta a^2)` integers, each with weight `O(log a/a)`. The resulting contribution to the quadratic form is therefore only `O(Delta log a)` by the trivial bound `Lambda(n)<=log n`. The lower taper lies below the first prime frequency once the scale is large.

The background part has the complementary continuum form. From `(13)`,

\[
\frac{2\Delta}{a}
\sum_{m=1}^K B(m\Delta)r_m
=
\frac2a\int_0^L e^\xi R_v(\xi)\,d\xi
+
O_{\psi,c}\!\left(
\mathcal L(v)\Delta
+
\frac{\log(1/\Delta)}a
\right).
\tag{23}
\]

Indeed the `e^xi` term is an ordinary weighted Riemann sum, whose error is `O(e^L \Delta \mathcal L(v))`; after division by `a` and `(3)` this is `O(\Delta \mathcal L(v))`. The second term in `(13)` behaves like `1/(4xi)` near zero and is exponentially integrable at infinity, so its complete normalized contribution is only

\[
O\!\left(\frac{\log(1/\Delta)}a\right)=o(1).
\tag{24}
\]

Thus the only potentially order-one quantity left in `(17)` is the difference between the `e^xi` continuum mass and the logarithmic prime-power measure.

## 3. The prime number theorem cancels the entire smooth continuum term

Let

\[
\Psi(x)
=
\sum_{n\le x}\Lambda(n).
\tag{25}
\]

The prime number theorem is equivalent to `Psi(x)=x+o(x)`. For the quantitative statement in `(4)`, the classical zero-free-region prime-number-theorem estimate gives, after partial summation from the corresponding estimate for `pi(x)`,

\[
\Psi(x)
=
x+
O\!\left(
x e^{-c_0\sqrt{\log x}}
\right)
\tag{26}
\]

for some absolute `c_0>0`.

Apply Stieltjes summation with

\[
F_v(x)
=
x^{-1/2}
R_v\!\left(\frac12\log x\right).
\tag{27}
\]

On the q-scale band `x<=e^{2L}=O_c(a^2)`, equation `(21)` gives

\[
|F_v'(x)|
\ll_\psi
\mathcal L(v)x^{-3/2}.
\tag{28}
\]

Writing `Psi(x)=x+E(x)`, integration by parts in `int F_v dE`, splitting once at `x=a`, and using `(26)` gives the interior estimate. After removing the endpoint strips just estimated, Stieltjes summation applies on the interior where `(21)` holds. Restoring the endpoints gives

\[
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
R_v(\lambda_n)
=
2\int_0^L e^\xi R_v(\xi)\,d\xi
+
O_{\psi,c}\!\left(
a\,\mathcal L(v)
e^{-c_1\sqrt{\log a}}
\right)
+
O_\psi(\Delta a\log a+1),
\tag{29}
\]

for some `c_1>0`. The factor `2` is forced by the logarithmic change of variables

\[
x=e^{2\xi},
\qquad
x^{-1/2}\,dx
=
2e^\xi\,d\xi.
\tag{30}
\]

Combining `(17)`, `(22)`, `(23)`, and `(29)` yields the uniform estimate

\[
\boxed{
\left|
v^\top\widehat T_Kv-1
\right|
\ll_{\psi,c}
\mathcal L(v)e^{-c_1\sqrt{\log a}}
+
\mathcal L(v)\Delta
+
\frac{\log(1/\Delta)}a
+
\Delta\log a.
}
\tag{31}
\]

Because `Delta asymp a^{-3}`, every family satisfying

\[
\mathcal L(v)
=
o\!\left(
e^{c_1\sqrt{\log a}}
\right)
\tag{32}
\]

obeys

\[
\boxed{
v^\top\widehat T_Kv=1+o(1).
}
\tag{33}
\]

In particular no such family can contain a negative Toeplitz witness. After slightly reducing `c_1` to absorb the implicit constants in `(31)`, any vector with

\[
v^\top\widehat T_Kv\le0
\tag{34}
\]

must satisfy the roughness lower bound `(4)`.

The nonquantitative core is even more robust. If one uses only `Psi(x)=x+o(x)`, then every family with uniformly bounded `\mathcal L(v)` still satisfies `(33)`. The zero-free-region error is needed only to turn qualitative roughness into the explicit subexponential scale in `(4)`.

## 4. Stress tests: the normalization is essential, and the theorem is not PSD

There are three important failure modes to exclude.

First, the conclusion is **not** true for an arbitrary unnormalized mesh bump for purely formal reasons. If

\[
p_\psi(u)=\sum_j\psi(j-u)
\tag{35}
\]

is not constant, then even a constant lag sequence `r_m=r` is mapped by the original XF-102 deposition to a mesh-phase factor `r p_psi(xi/Delta)`. That oscillates on the microscopic `Delta` scale. Classical PNT controls smooth logarithmic tests, not prime distribution against an arbitrarily fast mesh-phase oscillation. An apparent order-one q-scale Toeplitz signal in the unnormalized interface can therefore be an extractor-phase artifact. Equation `(9)` removes exactly that artificial degree of freedom before positivity is tested.

Second, `(33)` does **not** prove that `widehat T_K` is positive semidefinite. It says that every negative direction must have a rapidly varying lag autocorrelation. The remaining witness may exploit the arithmetic placement of prime powers relative to the mesh, short logarithmic intervals, or other rough correlations that disappear under continuum averaging. Those are precisely the structures that a Toeplitz/Caratheodory test beyond XF-107 now has to resolve.

Third, nothing here assumes RH. The cancellation in `(29)` uses only the classical prime number theorem. Under RH one would obtain a much sharper error for `Psi`, but importing that conditional gain would be inappropriate for the unconditional source-realizability gate.

As a numerical coefficient check, not as evidence, the transformed PNT term was evaluated for

\[
R_a(\xi)
=
\sin\!\left(\frac{\pi\xi}{\log a}\right),
\qquad
0\le\xi\le\log a.
\tag{36}
\]

The normalized residual

\[
\frac1a
\left[
2\int_0^{\log a}e^\xi R_a(\xi)\,d\xi
-
\sum_{n\le a^2}
\frac{\Lambda(n)}{\sqrt n}
R_a(\lambda_n)
\right]
\tag{37}
\]

was approximately `3.75e-3`, `8.55e-4`, `2.37e-4`, and `5.51e-5` for `a=30,100,300,1000`, respectively. This check catches the otherwise easy factor-of-two or sign error in `(29)` and is consistent with the exact asymptotic argument.

## 5. Consequence for the Xi-flow frontier

XF-106 showed that a negative principal Toeplitz witness below the first genuinely global regime needs

\[
|I|=\Omega(a)=\Omega(q^{1/2}).
\tag{38}
\]

XF-107 then showed that it must also span

\[
\ell
=
\Delta\,\operatorname{diam}(I)
\ge
\log a-O(1),
\tag{39}
\]

equivalently

\[
\operatorname{diam}(I)
=
\Omega(q^{3/2}\log q).
\tag{40}
\]

The present finding adds a third independent requirement after mass-preserving deposition:

\[
\boxed{
\mathcal L(v)
\ge
\exp\!\bigl(c\sqrt{\log q}\bigr)
}
\tag{41}
\]

after renormalizing the positive constant in the exponent.

This closes the naive continuum-operator continuation of XF-107. Looking only at the archimedean background `B(xi)~e^xi` suggests a q-scale integral operator with kernel `e^{|x-y|}` and large indefinite modes. That operator is not the source limit: the PNT main term of the prime-power measure cancels it on every sufficiently regular lag profile. **Any genuine source-Toeplitz failure must live in arithmetic roughness left after the prime-number-theorem main term is removed.**

The next useful source-side object is therefore not another smooth continuum kernel. It is a q-scale, collective, rough Toeplitz quadratic form that keeps the discrepancy

\[
d\Psi(x)-dx
\tag{42}
\]

rather than replacing either side by its main term. A successful negative witness there would be a genuine real-divisor obstruction. Conversely, a positivity estimate for that discrepancy-weighted rough sector would move the source realizability frontier materially beyond XF-107.

The load-bearing external ingredient added in this finding is the classical prime number theorem and its standard zero-free-region error, anchored in `SOURCES.md` through NIST DLMF §§25.16(i) and 27.12. A targeted search for Toeplitz moment positivity combined with logarithmic von-Mangoldt testing found no result matching the mass-preserving q-scale cancellation above; the nearest search hits concerned unrelated Toeplitz dynamical systems or generic Toeplitz operators. No novelty is claimed for PNT, Stieltjes summation, or partition-of-unity normalization separately. The line-specific contribution is the exact cancellation mechanism and the resulting roughness gate `(4)` for the Xi source moment problem.