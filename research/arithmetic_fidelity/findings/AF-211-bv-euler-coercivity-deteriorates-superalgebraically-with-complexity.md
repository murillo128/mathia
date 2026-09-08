# AF-211 — BV Euler coercivity deteriorates super-algebraically with source complexity

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-BRIDGE`, `QUANTITATIVE-FIDELITY`, `SOURCE-COMPLEXITY-GATE`, `SEVERE-ILL-POSEDNESS`, `NO-NOVELTY-CLAIM`

## Claim

AF-209 proves that every fixed bounded-variation complexity budget restores a positive lower recovery modulus for a positive-width Euler observation band. AF-210 then shows that, after such source compactification, the continuum band can be reduced to finitely many norming frequencies. Those statements are pointwise in the complexity budget. They do not give a useful modulus as the permitted source complexity grows.

For the same fixed parameters

\[
m\ge1,\qquad x>0,\qquad \sigma>0,\qquad 0<T<\infty,\qquad L>x,
\]

write

\[
\phi_\tau(t)=g_{m,\tau}(t)-g_{m,\tau}(x),
\qquad
h(t)=g_{m,0}(x)-g_{m,0}(t)>0\quad(t>x),
\]

and for `b in BV([x,L])` define

\[
D_T(b)
:=
\sup_{|\tau|\le T}
\left|\int_x^L\phi_\tau(t)b(t)\,dt\right|,
\qquad
V_h(b):=\int_x^L h(t)|b(t)|\,dt.
\]

Let the optimal AF-209 coercivity constant at BV budget `M` be

\[
\gamma(M)
:=
\inf\left\{
\frac{D_T(b)}{V_h(b)}:
0\ne b\in BV([x,L]),\
\operatorname{Var}(b)\le M V_h(b)
\right\}.
\tag{1}
\]

AF-209 gives

\[
\gamma(M)>0
\qquad\text{for every finite }M.
\tag{2}
\]

Nevertheless the dependence on `M` can be arbitrarily worse than every algebraic power:

\[
\boxed{
\forall p>0,\qquad
M^p\gamma(M)\longrightarrow0
\quad(M\to\infty).
}
\tag{3}
\]

Equivalently, for every integer `N>=1` there are constants `C_N,M_N<\infty`, depending only on the fixed Euler band and on one fixed interior test bump, such that

\[
\boxed{
0<\gamma(M)\le C_N M^{-N}
\qquad(M\ge M_N).
}
\tag{4}
\]

Thus there is no uniform inverse estimate of the form

\[
D_T(b)
\ge
c\,(1+\operatorname{Var}(b)/V_h(b))^{-p}V_h(b)
\tag{5}
\]

with fixed `c>0` and finite `p` on the full signed BV source cone.

The mechanism is not a new exact collision. Every finite `M` still has positive coercivity by AF-209. The new boundary is quantitative: a fixed smooth Euler band is an infinitely smoothing observation of increasingly oscillatory signed directions, so the inverse condition number along the AF-209 BV exhaustion grows faster than every algebraic complexity scale.

## Derivation

Choose once and for all

\[
x<a<b<L
\]

and a nonnegative, nonzero bump

\[
q\in C_c^\infty((a,b)).
\]

For integers `n>=1`, define the zero-mass oscillatory density

\[
r_n(t)
:=
\frac1n\frac{d}{dt}\bigl(q(t)\sin(nt)\bigr)
=
q(t)\cos(nt)+\frac{q'(t)}n\sin(nt).
\tag{6}
\]

Because `q` is compactly supported in `(a,b)`,

\[
\int_x^L r_n(t)\,dt=0.
\tag{7}
\]

### 1. The weighted source defect stays order one

Set

\[
v_n:=V_h(r_n).
\]

The pointwise inequality

\[
\left|
|r_n(t)|-q(t)|\cos(nt)|
\right|
\le \frac{|q'(t)|}{n}
\tag{8}
\]

implies

\[
v_n-
\int_a^b h(t)q(t)|\cos(nt)|\,dt
\longrightarrow0.
\tag{9}
\]

Periodic averaging gives

\[
\int_a^b h(t)q(t)|\cos(nt)|\,dt
\longrightarrow
\frac2\pi\int_a^b h(t)q(t)\,dt.
\tag{10}
\]

Hence

\[
\boxed{
v_n\longrightarrow
v_*:=\frac2\pi\int_a^b h(t)q(t)\,dt>0.}
\tag{11}
\]

In particular there are constants `0<v_-<v_+<infinity` with

\[
v_-\le v_n\le v_+
\tag{12}
\]

for all sufficiently large `n`.

### 2. BV complexity grows only linearly with frequency

Since `r_n` is smooth,

\[
\operatorname{Var}(r_n)=\int_x^L|r_n'(t)|\,dt.
\]

Differentiating `(6)`,

\[
r_n'(t)
=
-nq(t)\sin(nt)
+2q'(t)\cos(nt)
+\frac{q''(t)}n\sin(nt).
\tag{13}
\]

Therefore

\[
\operatorname{Var}(r_n)
\le
n\|q\|_1+2\|q'\|_1+n^{-1}\|q''\|_1
\le A_0 n
\tag{14}
\]

for all sufficiently large `n` and a fixed `A_0<infinity`. Combining with `(12)` gives

\[
\boxed{
\frac{\operatorname{Var}(r_n)}{V_h(r_n)}
\le A n
}
\tag{15}
\]

for a fixed `A<infinity`.

Thus the source complexity spent by the oscillatory direction is only first order in its frequency.

### 3. The smooth Euler band suppresses the same direction faster than every power

Using `(6)` and integrating by parts once,

\[
\int_x^L\phi_\tau(t)r_n(t)\,dt
=
-\frac1n
\int_a^b
\partial_t\phi_\tau(t)q(t)\sin(nt)\,dt.
\tag{16}
\]

For each fixed nonnegative integer `k`, the family

\[
A_\tau(t):=\partial_t\phi_\tau(t)q(t),
\qquad |\tau|\le T,
\]

has uniformly bounded `k`th `t`-derivative in `L^1([a,b])`. This follows because the Euler kernel is smooth on the compact rectangle `[-T,T] times [a,b]`, while `q` is a fixed smooth interior bump.

Because every derivative of `A_tau` vanishes at the endpoints of its compact support, repeated integration by parts in the oscillatory integral gives, for every integer `k>=0`,

\[
\sup_{|\tau|\le T}
\left|
\int_a^b A_\tau(t)\sin(nt)\,dt
\right|
\le B_k n^{-k}
\tag{17}
\]

with `B_k<infinity` independent of `n`. Substitution into `(16)` yields

\[
\boxed{
D_T(r_n)\le B_k n^{-(k+1)}.
}
\tag{18}
\]

After normalizing

\[
b_n:=\frac{r_n}{V_h(r_n)},
\tag{19}
\]

we have

\[
V_h(b_n)=1,
\qquad
\operatorname{Var}(b_n)\le An,
\qquad
D_T(b_n)\le C_R n^{-R}
\tag{20}
\]

for every prescribed integer `R>=1`, with a constant `C_R` depending on `R` but not on `n`.

### 4. Convert oscillation frequency into the AF-209 complexity budget

For sufficiently large `M`, choose

\[
n(M)=\left\lfloor\frac{M}{A}\right\rfloor.
\tag{21}
\]

After increasing the threshold if necessary,

\[
\operatorname{Var}(b_{n(M)})\le M,
\]

so `b_{n(M)}` is admissible in `(1)` with `V_h=1`. Also

\[
n(M)\ge\frac{M}{2A}
\tag{22}
\]

for all sufficiently large `M`. Hence for every integer `R>=1`,

\[
\gamma(M)
\le D_T(b_{n(M)})
\le C_R' M^{-R}.
\tag{23}
\]

This proves `(4)`. Given any real `p>0`, take an integer `R>p`; then

\[
0\le M^p\gamma(M)
\le C_R' M^{p-R}
\longrightarrow0,
\]

which proves `(3)`.

## Exact controls and boundaries

### AF-209 remains exactly correct at every fixed budget

The sequence above does not produce a nonzero element of the kernel of the positive-width Euler band. AF-209 proves that no such `L^1` density exists. Instead the sequence leaves every fixed compact BV-normalized class because

\[
\operatorname{Var}(b_n)\to\infty.
\]

The result therefore sharpens rather than contradicts AF-209:

\[
\boxed{
\text{finite complexity gives stable fidelity, but the stability constant is not algebraically uniform in complexity.}
}
\]

### This is stronger than the `O(n^{-1})` estimate used in AF-208 for the signed oscillatory component

AF-208 needed only one integration by parts because its purpose was to defeat coercivity while simultaneously carrying a separate mass-one anchor toward `x`. For the zero-mass interior component itself, smooth compact support permits arbitrarily many integrations by parts, exposing the rapid-decay mechanism hidden by that coarse estimate.

The mass-one anchor is not harmless for this stronger rate. The present theorem concerns the full signed BV cone appearing in AF-209. It does **not** prove super-algebraic deterioration on the narrower subclass of mass-one normalized Peano carriers used in AF-207/AF-208. Adding a concentrating unit-mass anchor introduces its own observation/variation scale and requires a separate conditioning analysis.

### AF-184 is a different super-algebraic obstruction

AF-184 obtains super-algebraic Euler invisibility using **positive parity-split point clusters whose cancellation order grows** as their spatial scale shrinks. The complexity resource there is cluster order/multiplicity and the source metric is normalized `W_1`.

Here the cancellation order of the source construction is not increased. One fixed smooth bump is modulated at higher frequency, the observation band and support interval remain fixed, and the complexity is exactly the BV budget introduced by AF-209. The two findings therefore expose the same broad smoothing pathology through different admissible source geometries rather than duplicating one theorem.

### No exponential rate is claimed

A generic `C_c^infty` bump has a Fourier transform that is rapidly decreasing but need not decay exponentially. Equation `(3)` is therefore the natural uniform conclusion from smoothness alone. Stronger Gevrey or analytic source restrictions would require separate assumptions and may produce different complexity laws.

### Exact recovery, stable recovery, and complexity-uniform recovery are three distinct gates

AF-209 already separated exact injectivity from fixed-class coercivity. AF-211 adds a third distinction:

\[
\boxed{
\text{exact injectivity}
\;\not\Rightarrow\;
\text{fixed-class stability}
\;\not\Rightarrow\;
\text{complexity-uniform conditioning}.
}
\]

The second implication is intentionally schematic: AF-209 supplies fixed-class stability after compactification, while AF-211 shows that the resulting constants can collapse faster than every power along a natural exhaustion of those compact classes.

## Prior art and novelty assessment

The analytic mechanism is classical and no novelty is claimed for rapid Fourier decay, compact smoothing operators, or singular-value decay from kernel regularity.

- Ching-Hua Chang and Chung-Wei Ha, **“Sharp inequalities of singular values of smooth kernels,”** *Integral Equations and Operator Theory* 35(1) (1999), 20–27, DOI `10.1007/BF01225525`, derive singular-value inequalities for smooth integral kernels and place smoothness-controlled spectral decay in the classical Gohberg–Krein tradition.
- Valdir A. Menegatto and C. P. Oliveira, **“Eigenvalue and singular value estimates for integral operators: a unifying approach,”** *Mathematische Nachrichten* 285 (2012), 2222–2232, DOI `10.1002/mana.201100257`, give an abstract framework in which kernel regularity forces decay of singular/eigenvalues and survey earlier smooth-kernel results.
- Darko Volkov, **“Optimal decay rates in Sobolev norms for singular values of integral operators,”** *Journal of Mathematical Analysis and Applications* 537(2) (2024), 128403, DOI `10.1016/j.jmaa.2024.128403`, gives modern optimal regularity-dependent singular-value estimates and treats smoother and analytic kernels separately.
- Rainer Kress, ***Linear Integral Equations***, 3rd ed., Springer (2014 printing of the 2013 edition), is standard background for compact first-kind integral equations and their inverse instability; AF-208 already uses this classical bridge.

The repeated-integration-by-parts proof above is more elementary than these singular-value theories and does not import their hypotheses. The durable Arithmetic Fidelity result is the exact specialization to the complexity gate introduced in AF-209: the optimal positive-width Euler coercivity constant on the BV cone is positive at every finite budget but tends to zero faster than every inverse polynomial of that budget.

## Consequences for Arithmetic Fidelity

The source-complexity gate is therefore not binary. Declaring a compactifying budget can turn exact recovery into a positive modulus, but the **dependence of that modulus on the budget is itself retained information about the inverse problem**. A proposed compression is not quantitatively faithful on a growing source family merely because every fixed complexity slice is individually recoverable.

For the current Euler branch, this supplies a concrete audit rule: whenever a later argument lets signed source complexity grow, it must carry a conditioning profile such as `gamma(M)` rather than quoting AF-209 pointwise. Any claimed polynomially controlled inverse, finite-resolution certificate, or asymptotic transfer across increasing BV budgets must confront `(3)` or introduce a stronger source restriction that excludes these oscillatory directions.

AF-210 remains valid on every declared precompact slice, but its finite norming reduction should likewise not be read as a complexity-uniform stability theorem. The observation family may be finitely normed after compactification while the best available separation margin simultaneously collapses super-algebraically as the compactified source class expands.