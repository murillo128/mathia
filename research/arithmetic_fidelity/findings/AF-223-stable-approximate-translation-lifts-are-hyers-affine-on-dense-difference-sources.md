# AF-223 — stable approximate translation lifts are Hyers-affine on dense-difference sources

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `QUANTITATIVE-FIDELITY`, `NEGATIVE/OBSTRUCTION`, `COORDINATE-RIGIDITY`, `CLASSICAL-BRIDGE`, `NO-NOVELTY-CLAIM`

## Claim

AF-221 and AF-222 show that an **exact** faithful scalar or vector-valued translation representation of the Euler profile cannot nonlinearly spread the collapsing rational-prime log-log mesh: dense source differences force the hidden coordinate onto one affine direction. The corresponding approximate question has an exact stability answer once the retained profile has a quantitative inverse modulus.

Let `V` be a real Banach space, `(Z,d_Z)` a metric space, `S\subset\mathbb R` a nonempty source set whose **difference set itself**

\[
S-S:=\{v-w:v,w\in S\}
\tag{1}
\]

is dense in `\mathbb R`, and let

\[
f:\mathbb R\to Z,
\qquad
\Phi:\mathbb R\to V,
\qquad
\Psi:S\to V,
\qquad
F:V\to Z,
\tag{2}
\]

with `\Phi` continuous. Suppose the difference lift reproduces the target profile with uniform error at most `\varepsilon`:

\[
\boxed{
 d_Z\!\left(
 F(\Phi(u)-\Psi(v)),
 f(u-v)
 \right)
 \le \varepsilon
 \qquad(u\in\mathbb R,\ v\in S).
}
\tag{3}
\]

Write

\[
\mathcal R
:=
\{\Phi(u)-\Psi(v):u\in\mathbb R,\ v\in S\}
\subset V
\tag{4}
\]

for the realized hidden states and define the realized inverse-resolution modulus

\[
\omega_F(r)
:=
\sup\{\|x-y\|:
 x,y\in\mathcal R,
 d_Z(F(x),F(y))\le r\}
\in[0,\infty].
\tag{5}
\]

Put

\[
\eta:=\omega_F(2\varepsilon).
\tag{6}
\]

If `\eta<\infty`, then there exist vectors `a,b,c\in V` such that

\[
\boxed{
\sup_{u\in\mathbb R}
\|\Phi(u)-(ua+b)\|
\le4\eta,
}
\tag{7}
\]

\[
\boxed{
\sup_{v\in S}
\|\Psi(v)-(va+c)\|
\le5\eta,
}
\tag{8}
\]

and, more directly on every source difference `d=v-w`,

\[
\boxed{
\|\Psi(v)-\Psi(w)-da\|
\le6\eta.
}
\tag{9}
\]

Moreover `b-c` is the affine hidden-state offset and

\[
\boxed{
\|\Phi(u)-\Psi(v)-((u-v)a+b-c)\|
\le5\eta
}
\tag{10}
\]

for all `u,v`.

Thus an approximately faithful translation lift is uniformly close to the same one-dimensional affine geometry whenever the profile does not hide large realized-state distances inside output errors of size `2\varepsilon`.

For a quantitatively faithful profile satisfying the lower Lipschitz bound

\[
d_Z(F(x),F(y))\ge m\|x-y\|
\qquad(x,y\in\mathcal R)
\tag{11}
\]

with `m>0`, one has

\[
\eta\le\frac{2\varepsilon}{m}.
\tag{12}
\]

Hence `(7)`--`(10)` become explicit `O(\varepsilon/m)` Hyers-Ulam bounds.

The rational-prime Euler source satisfies the stronger density hypothesis `(1)`. If

\[
v_p:=-\log\log p,
\tag{13}
\]

then

\[
\boxed{
S_{\mathbb P}-S_{\mathbb P}
\text{ is dense in }\mathbb R,
\qquad
S_{\mathbb P}:=\{v_p:p\text{ prime}\}.
}
\tag{14}
\]

Consequently, for consecutive primes `p<q`, `(9)` gives

\[
\|\Psi(v_p)-\Psi(v_q)\|
\le
\|a\|\,|v_p-v_q|+6\eta,
\tag{15}
\]

and therefore

\[
\boxed{
\limsup_{p\to\infty\atop q=p_{\rm next}}
\|\Psi(v_p)-\Psi(v_q)\|
\le6\eta.
}
\tag{16}
\]

In particular, if the hidden prime coordinates are required to have a uniform tail separation `c_*>0`, then necessarily

\[
\boxed{
\omega_F(2\varepsilon)\ge\frac{c_*}{6}.
}
\tag{17}
\]

Under the lower Lipschitz condition `(11)`, this implies the explicit error floor

\[
\boxed{
\varepsilon\ge\frac{m c_*}{12}.
}
\tag{18}
\]

So the exact coordinate obstruction of AF-221/AF-222 is stable: **a uniformly well-conditioned approximate translation representation cannot spread the vanishing prime-tail mesh with arbitrarily small error.** Any approximate escape must pay in at least one declared resource: nonvanishing observation error, deteriorating inverse conditioning of `F`, nontrivial unresolved fibers/side information, or departure from the one-difference translation category.

## Derivation

### 1. Approximate common target values collapse realized hidden states up to `eta`

For `v\in S` define

\[
Q_v(t):=\Phi(t+v)-\Psi(v).
\tag{19}
\]

Equation `(3)` becomes

\[
d_Z(F(Q_v(t)),f(t))\le\varepsilon.
\tag{20}
\]

Fix a base source point `v_0\in S` and set

\[
H(t):=Q_{v_0}(t).
\tag{21}
\]

For every `v` and `t`, the triangle inequality in `Z` gives

\[
d_Z(F(Q_v(t)),F(H(t)))\le2\varepsilon.
\tag{22}
\]

Both states lie in `\mathcal R`, so by `(5)`--`(6)`,

\[
\boxed{
\|Q_v(t)-H(t)\|\le\eta.
}
\tag{23}
\]

This is the quantitative replacement for the exact realized-state uniqueness used in AF-222. Exact injectivity is not enough for a stable statement; what matters is the diameter of the realized `2\varepsilon`-fibers.

Because `\Phi` is continuous and `v_0` is fixed, `H` is continuous.

### 2. Every direct source difference gives an almost-constant translation increment

Take `v,w\in S` and put

\[
d:=v-w.
\tag{24}
\]

For arbitrary `x`,

\[
Q_w(x+d)
=
\Phi(x+v)-\Psi(w),
\qquad
Q_v(x)
=
\Phi(x+v)-\Psi(v),
\tag{25}
\]

so

\[
Q_w(x+d)-Q_v(x)=\Psi(v)-\Psi(w).
\tag{26}
\]

Applying `(23)` to the two terms yields

\[
\boxed{
\|H(x+d)-H(x)-(\Psi(v)-\Psi(w))\|
\le2\eta.
}
\tag{27}
\]

Let

\[
h(t):=H(t)-H(0).
\tag{28}
\]

Putting `x=0` in `(27)` and comparing with `(27)` at general `x` gives

\[
\boxed{
\|h(x+d)-h(x)-h(d)\|
\le4\eta
\qquad(d\in S-S).
}
\tag{29}
\]

The important point is that no long word in the generated subgroup is needed. If `S-S` itself is dense, the error does not accumulate under repeated decomposition.

### 3. Density upgrades the restricted defect to a global approximate Cauchy equation

Fix `x,y\in\mathbb R`. By density of `S-S`, choose `d_n\in S-S` with `d_n\to y`. Continuity of `h` lets `(29)` pass to the limit:

\[
\boxed{
\|h(x+y)-h(x)-h(y)\|
\le4\eta
\qquad(x,y\in\mathbb R).
}
\tag{30}
\]

Thus the approximate translation representation has produced an ordinary uniform approximate Cauchy equation.

Hyers' classical stability theorem for Banach-valued approximately additive maps now gives an additive map

\[
A:\mathbb R\to V
\tag{31}
\]

such that

\[
\boxed{
\|h(t)-A(t)\|\le4\eta
\qquad(t\in\mathbb R).
}
\tag{32}
\]

For completeness, the usual proof applies directly: the sequence

\[
2^{-n}h(2^n t)
\tag{33}
\]

is Cauchy because the successive differences are bounded by `4\eta/2^n`, and its limit is additive with total deviation at most `4\eta`.

Since `h` is continuous and `A` stays within a fixed finite distance of `h`, `A` is locally bounded. A locally bounded additive map on `\mathbb R` is continuous and hence linear. Therefore there is `a\in V` such that

\[
A(t)=ta.
\tag{34}
\]

Combining `(32)` and `(34)`,

\[
\boxed{
\|H(t)-H(0)-ta\|\le4\eta.
}
\tag{35}
\]

### 4. Both sample and source coordinates are close to the same affine direction

Because `H(t)=\Phi(t+v_0)-\Psi(v_0)` exactly, set

\[
b:=H(0)+\Psi(v_0)-v_0a.
\tag{36}
\]

Writing `t=u-v_0` in `(35)` gives

\[
\|\Phi(u)-(ua+b)\|\le4\eta,
\tag{37}
\]

which is `(7)`.

For the source coordinate, take `v\in S`, put `d=v-v_0`, and compare `Q_v(0)` with `H(0)`. Equation `(23)` gives the sharper basepoint identity

\[
\|h(d)-(\Psi(v)-\Psi(v_0))\|
\le\eta.
\tag{38}
\]

Combining `(38)` with `(32)`--`(34)` gives

\[
\|\Psi(v)-\Psi(v_0)-da\|
\le5\eta.
\tag{39}
\]

Thus, with

\[
c:=\Psi(v_0)-v_0a,
\tag{40}
\]

we obtain `(8)`.

For arbitrary `v,w`, equation `(27)` at `x=0` gives

\[
\|\Psi(v)-\Psi(w)-h(v-w)\|\le2\eta.
\tag{41}
\]

Using `(32)`--`(34)` proves `(9)` with constant `6\eta`.

Finally `(23)` and `(35)` directly yield

\[
\|\Phi(u)-\Psi(v)-((u-v)a+H(0))\|
\le5\eta.
\tag{42}
\]

Since `(36)` and `(40)` give `b-c=H(0)`, this is `(10)`.

### 5. The rational-prime log-log source has dense direct differences

Let

\[
p_1<p_2<\cdots
\]

be the rational primes and

\[
v_n:=-\log\log p_n.
\tag{43}
\]

Then `v_n\downarrow-\infty`. AF-221 already records, using Bertrand's postulate, that

\[
0<v_n-v_{n+1}
=
\log\frac{\log p_{n+1}}{\log p_n}
\longrightarrow0.
\tag{44}
\]

This gives more than density of the subgroup generated by the differences. It makes the **direct difference set** dense.

Indeed, fix `r>0` and `\delta>0`. Choose `N` so that

\[
0<v_j-v_{j+1}<\delta
\qquad(j\ge N).
\tag{45}
\]

Choose `n>N` far enough that

\[
v_N-v_n>r.
\tag{46}
\]

Starting from `v_n` and moving upward through the tail, let `m\ge N` be the first index for which

\[
v_m-v_n\ge r.
\tag{47}
\]

The previous partial difference is below `r`, so the overshoot in `(47)` is at most the single mesh width `v_m-v_{m+1}<\delta`. Hence

\[
|(v_m-v_n)-r|<\delta.
\tag{48}
\]

Positive direct differences are therefore dense in `(0,\infty)`. Symmetry of `S-S` gives the negative half-line and zero is trivial, proving `(14)`.

### 6. Stable approximate coordinate stretching has a nonzero error floor

For consecutive primes, `(44)` and `(9)` imply `(15)`, hence `(16)`.

If the reparameterized prime source is required to satisfy

\[
\|\Psi(v_p)-\Psi(v_q)\|\ge c_*>0
\tag{49}
\]

for every sufficiently large consecutive pair, then `(16)` forces `(17)`.

When `(11)` holds, every pair counted in `(5)` satisfies

\[
\|x-y\|\le\frac{d_Z(F(x),F(y))}{m},
\]

so `(12)` follows. Combining `(12)` with `(17)` gives `(18)`.

The obstruction is therefore not only exact. Uniform tail spreading can coexist with increasingly accurate approximation only if the inverse resolution of the retained profile simultaneously deteriorates. In Arithmetic Fidelity language, the proposed extra coordinate then lives in a direction that the scalar observation resolves more and more poorly; it has become unstable side information rather than a well-conditioned reparameterization.

## Exact controls and boundaries

### Dense `S-S` is stronger than dense generated subgroup

AF-221/AF-222 need only density of `\langle S-S\rangle` in the exact problem because zero error can be composed through arbitrarily many source differences. With nonzero error, that argument would accumulate the defect with word length. AF-223 therefore assumes density of the direct difference set itself. The rational-prime log-log source satisfies this stronger condition by `(43)`--`(48)`.

### Stable inverse resolution is the real approximate-fidelity gate

Exact injectivity of `F|_\mathcal R` gives only `\omega_F(0)=0`. It does not imply that `\omega_F(r)\to0` at a useful rate as `r\downarrow0`. AF-223 deliberately exposes this conditioning requirement instead of hiding it inside the word "faithful".

A family of exact or approximate lifts can therefore evade a uniform version of the theorem by making the inverse condition number blow up. That is a genuine stability failure, not preservation of the old coordinate at fixed quality.

### The theorem does not prohibit genuine side information

If `F` has large or nontrivial realized fibers at the observation scale, `\eta` is large and the theorem becomes weak. Extra marks, provenance labels, transverse coordinates, or relational information can live in those fibers. AF-223 classifies that possibility as an enrichment of the retained state rather than a stable coordinate warp.

### Banach completeness enters only through Hyers stability

The initial hidden-state collapse `(23)` and approximate increment law `(27)` require only a normed target. Completeness is used to take the Hyers limit `(33)`. Other complete metric-group or topological-vector-space stability theorems may provide analogous variants, but they are not claimed here.

### Uniform error over the full translation family is essential

Equation `(3)` holds for every real sample coordinate and every source point. A finite sampled matrix, a local window, a source-dependent profile, or an error bound that deteriorates along the prime tail is a different approximation category. AF-223 does not silently promote finite-window fitting to a global stable representation.

### The constants are sufficient, not advertised as globally optimal

The factors `4`, `5`, and `6` come from two triangle-inequality comparisons followed by the classical Hyers bound. The theorem needs only their uniform finiteness and vanishing with `\eta`; no sharp-constant novelty is claimed.

### No RH consequence is claimed

The result concerns stability of a translation-coordinate representation. It does not locate zeta zeros or provide a prime-discriminator theorem. Its role is to close an approximate version of a coordinate escape exposed by AF-220--AF-222 and to identify exactly what must become ill-conditioned if that escape is attempted.

## Prior art and novelty assessment

The central stability mechanism is classical.

- Donald H. Hyers, **“On the Stability of the Linear Functional Equation,”** *Proceedings of the National Academy of Sciences of the United States of America* **27**(4), 222–224 (1941), DOI `10.1073/pnas.27.4.222`, proves the foundational uniform stability theorem for approximately additive Banach-space-valued maps used in `(30)`--`(35)`.
- János Aczél, ***Lectures on Functional Equations and Their Applications***, Academic Press (1966), and János Aczél with Jean Dhombres, ***Functional Equations in Several Variables***, Cambridge University Press (1989), are standard references for Cauchy/Pexider rigidity and regularity of additive solutions.
- Abbas Najati, M. R. Abdollahpour, and Gwang Hui Kim, **“On Pexider Differences in Topological Vector Spaces,”** *Abstract and Applied Analysis* 2011, Article ID 370104, DOI `10.1155/2011/370104`, is neighboring prior art for Pexiderized functional equations and their stability in topological-vector-space settings.
- Abbas Najati, Jung Im Kang, and Yeol Je Cho, **“Local stability of the Pexiderized Cauchy and Jensen's equations in fuzzy spaces,”** *Journal of Inequalities and Applications* 2011, Article 78, DOI `10.1186/1029-242X-2011-78`, illustrates the broader established Hyers-Ulam literature for Pexiderized Cauchy equations, including restricted-domain stability questions.

A targeted literature search confirms that approximate Cauchy/Pexider rigidity is a mature theory. No novelty is claimed for Hyers stability, Pexider stability, or for the elementary triangle-inequality conversion from common approximate observations to an approximate Pexider relation.

The durable Arithmetic Fidelity delta is the **category-specific composition of these classical ingredients**: the realized inverse-resolution modulus `(5)` converts output error into hidden-state defect, dense direct source differences prevent word-length error accumulation, and the rational-prime log-log source satisfies that direct-density hypothesis. This yields the explicit prime-tail error floor `(17)`--`(18)` and turns the informal phrase "approximate coordinate stretching" into a falsifiable conditioning statement.

## Relation to AF-220--AF-222

AF-220 shows that finite-order Euler sign regularity can be certified from curvature and source/sample separation, but that the canonical consecutive-prime log-log mesh collapses in the tail. AF-221 proves that an exact faithful scalar translation coordinate cannot nonlinearly stretch that mesh, and AF-222 extends the exact obstruction to faithful vector-valued hidden states.

AF-223 closes the corresponding stable-approximation gap. Exact fidelity is recovered at `\varepsilon=0` when the realized profile fibers are singletons. More importantly, for `\varepsilon>0` it shows that a coordinate escape is useful only to the extent that the downstream profile can resolve the added separation. If the profile remains uniformly well conditioned, the lift stays Hyers-close to one affine direction and the prime-tail mesh still collapses up to an explicitly controlled residual.

The remaining admissible frontier is therefore sharper: obtain a genuine source-side arithmetic restriction, retain nontrivial relational/provenance information in intentionally non-singleton fibers, or leave the pure one-difference translation category. Merely making the existing coordinate higher-dimensional, nonlinear, or approximately fitted is not an independent stable resource.