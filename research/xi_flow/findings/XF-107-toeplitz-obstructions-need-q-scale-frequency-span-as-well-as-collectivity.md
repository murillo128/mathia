# XF-107 — Toeplitz obstructions need q-scale frequency span as well as collectivity

**Status:** `EXACT-DERIVED` + `TOEPLITZ-DELOCALIZATION` + `ARITHMETIC-SCALE-BOUNDARY` + `COLLECTIVE-WIDE-OBSTRUCTION`. XF-105 showed that the fixed raw-`ell^1` equal-weight cone reaches a deterministic wall at a fixed fraction of the natural `q` arithmetic scale. XF-106 then showed that failure of the less-lossy Toeplitz/Caratheodory gate cannot be local in *cardinality*: throughout the natural scale, any negative Toeplitz witness needs `Omega(a)=Omega(q^{1/2})` moment coordinates. There is a second, independent delocalization requirement. A negative witness cannot be dense but confined to a short interval of Vieta indices either.

Keep

\[
N=2q^2,
\qquad
\Delta^2\asymp q^{-3},
\qquad
a:=N\Delta\asymp q^{1/2},
\tag{1}
\]

and the distribution-safe endpoint moments from XF-102--XF-106,

\[
Q_m^\psi
=
B(m\Delta)
-
\frac1{2\Delta}
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\psi\!\left(\frac{m\Delta-\lambda_n}{\Delta}\right),
\qquad
\lambda_n=\frac12\log n,
\tag{2}
\]

with fixed bounded `psi` supported in `[-1,1]`. Normalize

\[
\mu_0=1,
\qquad
\mu_m=\frac{Q_m^\psi}{N},
\qquad
\mu_{-m}=\overline{\mu_m},
\tag{3}
\]

and let `T_K=(mu_{i-j})_{0<=i,j<=K}` be the XF-084 Toeplitz moment matrix.

For an arbitrary principal coordinate set

\[
I\subset\{0,\ldots,K\},
\qquad
s:=|I|,
\qquad
d:=\max I-\min I,
\qquad
\ell:=d\Delta,
\tag{4}
\]

one has the **diameter-sensitive** lower bound

\[
\boxed{
\lambda_{\min}(T_I)
\ge
1-
C_\psi\,
\frac{e^\ell+\ell+\log(d+1)+1}{a}.
}
\tag{5}
\]

The constant is independent of the location of `I`, its cardinality, and the ambient prefix length. In particular, if

\[
\ell\le \log a-r(a),
\qquad
r(a)\longrightarrow+\infty,
\tag{6}
\]

then uniformly over **every** such principal set,

\[
\boxed{
\lambda_{\min}(T_I)=1-o(1).
}
\tag{7}
\]

There is no cardinality restriction in `(7)`: `I` may contain every coordinate in its interval, so its size may be of order `Delta^{-1} log a`, vastly larger than the `Omega(a)` scale isolated by XF-106.

Consequently any negative Toeplitz principal minor must have

\[
\boxed{
\ell=d\Delta\ge \log a-O_\psi(1).
}
\tag{8}
\]

Since the explicit-formula arithmetic frequency is `lambda_n=(log n)/2`, `(8)` means that any weighted-measure obstruction must span arithmetic scale

\[
\boxed{
e^{2\ell}\gg_\psi a^2\asymp q.}
\tag{9}
\]

Combining `(8)` with XF-106 in its pointwise-dilute range gives the two simultaneous necessary conditions, at the natural `q` scale,

\[
\boxed{
|I|=\Omega(q^{1/2}),
\qquad
\operatorname{diam}(I)
=\Omega(q^{3/2}\log q).
}
\tag{10}
\]

Thus the next Toeplitz gate is not merely high-dimensional. It is **q-scale delocalized in lag space**: no bounded physical frequency window, no prime-free block, no fixed finite collection of prime bands, and in fact no band ending a diverging amount below `log a` can carry a negative certificate, even if that band contains all of its `Theta(Delta^{-1} log a)` coordinates.

## 1. A principal Toeplitz block only sees moments up to its lag diameter

Fix `I` as in `(4)`. For each row indexed by `i in I`, every off-diagonal entry has the form `mu_{i-j}` with

\[
1\le |i-j|\le d.
\]

For each positive lag `m`, there are at most two entries in a given row with `|i-j|=m`. Hence

\[
\max_{i\in I}
\sum_{\substack{j\in I\\j\ne i}}
|\mu_{i-j}|
\le
2\sum_{m=1}^{d}|\mu_m|.
\tag{11}
\]

The Rayleigh quotient or Gershgorin therefore gives

\[
\boxed{
\lambda_{\min}(T_I)
\ge
1-2\sum_{m=1}^{d}|\mu_m|.
}
\tag{12}
\]

The point is that `(12)` depends on the **difference set** of the support, not on where the support sits inside the much larger ambient matrix. A translated dense block and the initial dense block of the same diameter obey exactly the same estimate.

## 2. Chebyshev mass control applies to every lag window, not only the full visible prefix

XF-104 derived, for a prefix with physical cutoff `L`,

\[
\sum_{m\le L/\Delta}|B(m\Delta)|
\ll
\Delta^{-1}
\bigl(e^L+L+\log(L/\Delta+2)+1\bigr),
\tag{13}
\]

and the elementary Chebyshev bound

\[
\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}
\ll \sqrt X.
\tag{14}
\]

These estimates do not require that `L` be the outer cutoff of the whole state. Apply them only to the lags `1<=m<=d` occurring in `(11)`. Because `supp psi subset [-1,1]`, each prime-power atom contributes to at most three mesh sites, and only atoms with

\[
\lambda_n\le \ell+\Delta
\]

can enter. Therefore `(14)` gives

\[
\begin{aligned}
&\sum_{m=1}^{d}
\left|
\frac1{2\Delta}
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\psi\!\left(\frac{m\Delta-\lambda_n}{\Delta}\right)
\right|\\
&\hspace{3cm}\ll_\psi
\Delta^{-1}e^{\ell+\Delta}.
\end{aligned}
\tag{15}
\]

Using `(13)` with `L=ell` and combining with `(15)`,

\[
\sum_{m=1}^{d}|Q_m^\psi|
\ll_\psi
\Delta^{-1}
\bigl(e^\ell+\ell+\log(d+1)+1\bigr).
\tag{16}
\]

Since

\[
N=\frac a\Delta,
\tag{17}
\]

normalization turns `(16)` into

\[
\boxed{
\sum_{m=1}^{d}|\mu_m|
\ll_\psi
\frac{e^\ell+\ell+\log(d+1)+1}{a}.
}
\tag{18}
\]

Equations `(12)` and `(18)` prove `(5)`.

No prime number theorem, zero-free region, or RH input enters. The only arithmetic estimate is the same Chebyshev-level bound already derived inside XF-104.

## 3. Every sub-q-scale lag window is uniformly deep inside the Toeplitz cone

Assume `(6)`. Then `ell=O(log a)`. Since `Delta asymp a^{-3}`, one has

\[
d\le \frac{\log a}{\Delta},
\qquad
\log(d+1)=O(\log a).
\tag{19}
\]

Consequently

\[
\frac{\ell+\log(d+1)+1}{a}=o(1),
\tag{20}
\]

while

\[
\frac{e^\ell}{a}
\le e^{-r(a)}
\longrightarrow0.
\tag{21}
\]

Substitution into `(5)` yields `(7)` uniformly over all principal coordinate sets with that diameter.

A useful concrete calibration is

\[
\ell
=
\log a-2\log\log a.
\tag{22}
\]

Then the associated complete arithmetic range is

\[
e^{2\ell}
=
\frac{a^2}{(\log a)^4}
\asymp
\frac q{(\log q)^4},
\tag{23}
\]

and yet every Toeplitz principal block whose lag span stays inside that range satisfies

\[
T_I=I+o_{\rm op}(1)
\tag{24}
\]

with no restriction on `|I|`. In particular a **fully dense** block can have

\[
|I|\asymp d
\asymp
\Delta^{-1}\log a
\asymp
q^{3/2}\log q
\tag{25}
\]

and still converge spectrally to the identity. This is much stronger than applying XF-106's `s=o(a)` sparse-minor estimate to the same block.

The fixed-physical-band case is an even simpler corollary. For every fixed `Lambda_*>0`, all principal blocks with

\[
d\Delta\le\Lambda_*
\]

obey

\[
\lambda_{\min}(T_I)
=1-O_{\Lambda_*,\psi}\!\left(\frac{\log a}{a}\right).
\tag{26}
\]

So the first prime frequency `log 2/2`, or any fixed finite collection of prime-power frequencies, is far too local in lag space to create a weighted-measure obstruction.

## 4. A negative witness must reach the natural q arithmetic scale

Suppose now that `T_I` has a negative eigenvalue. Equation `(12)` forces

\[
2\sum_{m=1}^{d}|\mu_m|>1.
\tag{27}
\]

Combining with `(18)`,

\[
e^\ell+\ell+\log(d+1)+1
\gg_\psi a.
\tag{28}
\]

If `ell>=log a`, `(8)` is immediate. Otherwise `ell<log a`, so as in `(19)`,

\[
\ell+\log(d+1)+1=O(\log a)=o(a).
\tag{29}
\]

Equation `(28)` therefore requires

\[
e^\ell\gg_\psi a,
\]

which is exactly `(8)`.

The corresponding index diameter is

\[
d
\ge
\frac{\log a-O_\psi(1)}{\Delta}.
\tag{30}
\]

Using `Delta^{-1} asymp q^{3/2}` and `log a=(1/2+o(1))log q`,

\[
\boxed{
d=\Omega_\psi(q^{3/2}\log q).}
\tag{31}
\]

Meanwhile `lambda_n=(log n)/2` converts `(8)` into `(9)`. The Toeplitz failure cannot be witnessed by arithmetic information whose complete span stops at `q/polylog(q)` or any smaller `q e^{-omega(1)}` scale. It has to reach a fixed multiplicative fraction of the natural `q` scale at minimum.

## 5. XF-106 adds an independent cardinality obstruction

The diameter estimate used only the cumulative prefix mass. XF-106 supplies a different control. In the pointwise-dilute band

\[
\ell
\le
\left(\frac32-\eta\right)\log a,
\qquad \eta>0\text{ fixed},
\tag{32}
\]

it proves

\[
\varepsilon_a
:=
\max_{1\le m\le d}|\mu_m|
\ll_{\eta,\psi}a^{-1}.
\tag{33}
\]

Therefore

\[
\lambda_{\min}(T_I)
\ge
1-(s-1)\varepsilon_a.
\tag{34}
\]

Combining `(12)` and `(34)` gives the two-parameter estimate

\[
\boxed{
\lambda_{\min}(T_I)
\ge
1-
\min\!\left\{
(s-1)\varepsilon_a,
\;2\sum_{m=1}^{d}|\mu_m|
\right\}.
}
\tag{35}
\]

Hence any negative witness inside `(32)` must satisfy **both**

\[
s=\Omega_{\eta,\psi}(a)
\tag{36}
\]

and `(8)`. The natural `q`-scale regime `ell=log a+O(1)` lies comfortably inside `(32)` for any fixed `eta<1/2`. Translating `(36)` and `(31)` to the original Xi parameters yields `(10)`.

These are genuinely different requirements. A witness may be highly collective but concentrated in a short run of coordinates; `(5)` rules that out. Or it may span the entire q-scale band but use only a sparse set of coordinates; XF-106 rules that out until the support reaches `Omega(q^{1/2})`. A possible Toeplitz obstruction must coordinate a large set **across** a very long lag interval.

## 6. Stress tests and evidence boundary

This finding does **not** prove global Toeplitz positivity at `ell=log a+O(1)`. At that scale the right side of `(18)` is only `O(1)`, exactly where absolute row-sum control ceases to decide the sign. A collective q-scale matrix may still be indefinite. Equation `(8)` says where a negative certificate is first allowed to live, not that one exists there.

There is no contradiction with XF-105. Its lower bound shows that the global raw `ell^1` mass already reaches a fixed constant near `L=log a+O(1)` because the untouched archimedean background accumulates over a huge number of mesh cells. The present result says that this cumulative wall cannot be converted into a negative Toeplitz minor inside a substantially shorter lag span. Failure of the XF-085 sufficient cone remains distinct from failure of the weighted-measure positivity gate.

Nor does `(7)` extend the XF-104 collision-crystal nonidentifiability theorem automatically. Toeplitz PSD is only the weighted-measure relaxation from XF-084; exact equal-weight realization at the prescribed degree is stronger. The present theorem narrows where that relaxation can fail but does not construct a carrier beyond the already proved equal-weight cone.

The compact support and boundedness of `psi` are used only in `(15)` to ensure that each prime-power atom touches `O(1)` mesh cells. Its sign is irrelevant for the upper bound. The result therefore persists for any fixed-width distribution-safe atomic extractor with uniformly bounded overlap and amplitudes.

Finally, nothing here advances the separate destination-coercivity problem. XF-098--XF-104 show that large classes of periodic collision geometry remain invisible to low Vieta histories. The present result concerns only the source-side real-divisor feasibility gate that arose after those negative controls.

## 7. Prior-art boundary and consequence for the frontier

The Toeplitz moment criterion, Caratheodory/Herglotz interpretation, and weighted-measure relaxation are classical and already anchored by XF-084. The matrix step `(11)`--`(12)` is elementary Gershgorin/Rayleigh control, while the number-theoretic input `(14)` is the Chebyshev estimate already derived in XF-104. A targeted literature check of recent Riemann/Toeplitz work found Connes--Consani's use of Hermitian Toeplitz matrices in archimedean Weil positivity and recent Toeplitz-minor results for the Taylor coefficients of xi, but these concern different Toeplitz objects and do not provide the mesh-scale Vieta estimate `(5)` or the q-scale support requirement `(8)`--`(10)`. No new external theorem is load-bearing, so `SOURCES.md` requires no change.

The durable line-specific conclusion is that XF-106's word **collective** can now be made two-dimensional. A possible failure of the Xi-derived Toeplitz moment cone must be collective in the number of coordinates and delocalized in their lag geometry. At the natural scale it needs at least `Omega(q^{1/2})` participating coordinates spread across `Omega(q^{3/2} log q)` Vieta indices, reaching arithmetic frequencies corresponding to `n asymp q`.

That changes the next useful source-side test. Searching for a small principal minor, a dense fixed-frequency block, or a finite-prime obstruction cannot succeed. The informative object is a genuinely q-scale collective quadratic form, or an operator/continuum limit that retains correlations across the entire `ell=log a+O(1)` band. The fixed raw-`ell^1` wall of XF-105 and the sparse-minor exclusion of XF-106 are therefore not competing diagnoses; together they locate the first scale on which the Toeplitz feasibility question can become nontrivial.