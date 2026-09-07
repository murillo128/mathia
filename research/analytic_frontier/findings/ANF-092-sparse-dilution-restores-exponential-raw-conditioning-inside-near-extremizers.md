# ANF-092 — sparse dilution restores exponential raw conditioning inside near-extremizers

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + NEAR-EQUALITY-CONTROL + SEPARABLE-CONE + SPARSE-CONDITIONING-BLOCK + ALL-CARDINALITIES + RAW-RATIO-OBSTRUCTION`. `ANF-090` shows that the raw cross-metric ratio `chi_s=b_s/a` can blow up exponentially on a dense two-row product chain, but that chain is not Montgomery--Taylor near-extremal. `ANF-091` then proves that positive-density subunit crowding is incompatible with near equality and leaves open only a vanishing-density conditioning component. That remaining loophole is genuine: one can dilute the `ANF-090` finite-difference block inside a much larger real near-extremal comb, lift the whole horizontal set to one common conjugate height tending slowly enough to zero, and obtain configurations that are simultaneously exactly separable, Montgomery--Taylor near-extremal, and exponentially ill-conditioned for the raw ratio.

Fix any

\[
0<d<1,
\qquad
r:=\sin\frac{\pi d}{2}\in(0,1).
\tag{1}
\]

There exists an explicit sequence of finite two-row product multisets

\[
W_n=X_n+i\{-y_n,+y_n\}
\tag{2}
\]

such that

\[
\boxed{
\frac{\Delta(W_n)}{L(W_n)}\longrightarrow0,
\qquad
d_{\rm sep}(W_n)=0,
\qquad
\chi_s(W_n)\longrightarrow\infty
}
\tag{3}
\]

and in fact `chi_s(W_n)` grows exponentially. Moreover the very product appearing on the right side of the `ANF-089` estimate diverges:

\[
\boxed{
\chi_s(W_n)\,\frac{\Delta(W_n)}{L(W_n)}\longrightarrow\infty.
}
\tag{4}
\]

Thus neither near-extremality nor multiplication by the relative Montgomery--Taylor excess repairs the unquotiented condition number. The raw real-collapse comparison of `ANF-089` can be arbitrarily badly conditioned even on a sequence lying exactly in the safe separable cone and approaching the sharp Montgomery--Taylor floor. The separable quotient is therefore mathematically necessary rather than merely a desirable refinement.

## 1. A high-zero arithmetic comb supplies arbitrarily large real near-extremal padding

Retain the exact Montgomery--Taylor factor from `ANF-087`,

\[
K(x)=
\frac{\cos(\pi x)-a x\sin(\pi x)}{1-2\pi^2x^2},
\qquad
a:=\sqrt2\,\pi\cot(2^{-1/2})>0,
\tag{5}
\]

whose positive zeros are

\[
r_N=N+\varepsilon_N,
\qquad 0<\varepsilon_N<\frac12,
\qquad
\tan(\pi\varepsilon_N)=\frac1{a r_N}.
\tag{6}
\]

Since `tan t>=t` on `[0,pi/2)`,

\[
0<\varepsilon_N\le\frac1{a\pi N}.
\tag{7}
\]

A useful uniform consequence is that there is a constant `C_K`, depending only on the fixed Montgomery--Taylor profile, such that

\[
\boxed{
|K(mr_N)|\le\frac{C_K}{N^2}
\qquad(N\ge1,\ m\ge2).
}
\tag{8}
\]

Indeed, if `2<=m<=N`, then

\[
|\sin(\pi m\varepsilon_N)|
\le \pi m\varepsilon_N
\le\frac{m}{aN},
\tag{9}
\]

so the numerator in (5) is `O(m^2)` while the denominator is `Omega(m^2N^2)`. If `m>N`, use only `|sin|<=1`; the numerator is `O(mN)` and the denominator is `Omega(m^2N^2)`, again giving `O(N^{-2})`. The case `m=1` is better: `K(r_N)=0` exactly.

Now put

\[
q_n:=n^3,
\qquad
N_n:=n^3,
\qquad
T_n:=n^{10},
\tag{10}
\]

and define a large high-zero comb

\[
H_n:=\{T_n+jr_{N_n}:0\le j<q_n\}.
\tag{11}
\]

Its real Montgomery--Taylor off-diagonal energy is

\[
2\sum_{1\le i<j\le q_n}K((j-i)r_{N_n})^2
=O\!\left(\frac{q_n^2}{N_n^4}\right)
=O(n^{-6}).
\tag{12}
\]

The point is not that the zero set contains long arithmetic progressions—it does not—but that multiples of one sufficiently high zero have `K`-value uniformly `O(N^{-2})`. Hence the sharp real floor admits arbitrarily large supports with vanishing *relative* excess even though exact equality has at most two sites by `ANF-087`.

## 2. Dilute one dense finite-difference block into that padding

Let

\[
C_n:=\{0,d,2d,\ldots,nd\},
\qquad
X_n:=C_n\cup H_n,
\qquad
A_n:=|X_n|=q_n+n+1.
\tag{13}
\]

All sites are simple for large `n`. Because `K=\widehat g` with `g>=0` and `\int g=1`,

\[
|K(x)|\le1
\qquad(x\in\mathbb R).
\tag{14}
\]

Thus the complete dense-block contribution to `E_MT(X_n)-A_n` is `O(n^2)`. Equation (12) gives `O(n^{-6})` for the high-zero comb. Finally the explicit formula (5) gives

\[
|K(x)|\le\frac{C_0}{|x|}
\qquad(|x|\ge1)
\tag{15}
\]

for a fixed `C_0`; every cross distance between `C_n` and `H_n` is at least `T_n-nd`, so the cross contribution is

\[
O\!\left(
\frac{(n+1)q_n}{(T_n-nd)^2}
\right)
=O(n^{-16}).
\tag{16}
\]

Consequently

\[
\boxed{
\frac{E_{\rm MT}(X_n)}{A_n}=1+O(n^{-1}).
}
\tag{17}
\]

The dense `d`-spaced block has only `O(n)` sites inside a support of size `Theta(n^3)`. It is therefore invisible to the relative energy budget even though it retains exactly the finite-difference geometry responsible for the conditioning loss in `ANF-090`.

## 3. A slowly collapsing common height preserves near equality

Choose

\[
\boxed{y_n:=r^{n/8}.}
\tag{18}
\]

Form the two-row product multiset (2). It has `|W_n|=2A_n`, no real sites, and therefore

\[
L(W_n)=4A_n.
\tag{19}
\]

Its structure factor is

\[
S_{W_n}(\alpha)
=2\cosh(2\pi\alpha y_n)A_{X_n}(\alpha).
\tag{20}
\]

Since the Montgomery--Taylor spectrum is nonnegative and supported on `[-1,1]`,

\[
E_{\rm MT}(W_n)
\le
4\cosh^2(2\pi y_n)E_{\rm MT}(X_n).
\tag{21}
\]

Combining (17), (19), and `cosh^2 u=1+O(u^2)` at the origin gives

\[
0\le
\frac{\Delta(W_n)}{L(W_n)}
\le
\cosh^2(2\pi y_n)
\frac{E_{\rm MT}(X_n)}{A_n}-1
=O(n^{-1})+O(r^{n/4}),
\tag{22}
\]

which proves the first limit in (3).

At the same time `W_n` is exactly of the product form covered by `ANF-085`, so

\[
\boxed{d_{\rm sep}(W_n)=0}
\tag{23}
\]

for every `n`. This sequence is a control family, not a central-notch counterexample.

## 4. The sparse block still forces exponential raw conditioning

The source Gram minimum `a(W_n)` from `ANF-089` is bounded above by any Rayleigh vector supported on a subset of the full support. Use the same normalized binomial finite difference as `ANF-090`, supported only on the upper row above `C_n`. With

\[
A_y:=\int_{-1/2}^{1/2}
\eta_{\rm MT}(u)^2e^{4\pi uy}\,du,
\tag{24}
\]

that calculation gives

\[
a(W_n)
\le
A_{y_n}(2n+1)r^{2n}.
\tag{25}
\]

Because `y_n<=1` eventually and `\int\eta_{\rm MT}^2=1`,

\[
A_{y_n}\le e^{2\pi}.
\tag{26}
\]

For the destination defect Gram, every nonreal pair has the same height `y_n`; hence any diagonal entry gives

\[
b_s(W_n)
\ge
B_{s,y_n}
:=4\int_{-1}^{1}J_s(\alpha)
\bigl(\cosh(2\pi\alpha y_n)-1\bigr)^2\,d\alpha.
\tag{27}
\]

Using `cosh t-1>=t^2/2`,

\[
B_{s,y}
\ge
(2\pi)^4y^4
\int_{-1}^{1}J_s(\alpha)\alpha^4\,d\alpha
=:c_s y^4,
\qquad c_s>0.
\tag{28}
\]

Therefore (18), (25)--(28) imply

\[
\boxed{
\chi_s(W_n)
=\frac{b_s(W_n)}{a(W_n)}
\ge
\frac{c_s}{e^{2\pi}(2n+1)}
\,r^{-3n/2}
\longrightarrow\infty.
}
\tag{29}
\]

The collapse height tends to zero, so the diagonal destination defect itself shrinks like `y_n^4`; nevertheless the source finite-difference direction shrinks much faster, like `r^{2n}`. The ratio therefore still diverges exponentially.

## 5. Even the raw `chi_s` times excess factor diverges

The upper estimate (22) proves near-extremality, but `ANF-091` also gives a polynomial *lower* obstruction from the dense block. Its `n` adjacent horizontal pairs have separation exactly `d<1`, so equation (7) of `ANF-091` yields

\[
\frac{\Delta(W_n)}{L(W_n)}
\ge
\frac{2n}{A_n}K(d)^2.
\tag{30}
\]

The first positive zero of `K` lies beyond `1`, so `K(d)\ne0`. Since `A_n=Theta(n^3)`,

\[
\frac{\Delta(W_n)}{L(W_n)}
\gg n^{-2}.
\tag{31}
\]

Combining (29) and (31),

\[
\boxed{
\chi_s(W_n)
\frac{\Delta(W_n)}{L(W_n)}
\gg
\frac{r^{-3n/2}}{n^3}
\longrightarrow\infty,
}
\tag{32}
\]

which proves (4). Thus the right side of the general real-collapse estimate

\[
d_{\rm sep}(W)^2
\le
\frac{\chi_s(W)}{2q_s}
\frac{\Delta(W)}{L(W)}
\tag{33}
\]

can diverge while its left side is identically zero. This is stronger than `ANF-090`: restricting to the Montgomery--Taylor near-extremizer regime does not make the raw proof constant informative.

## 6. Adversarial checks, prior-art boundary, and consequence

The construction uses only positive multisets; the alternating binomial coefficients appear solely as an admissible Rayleigh vector for the source Gram matrix, exactly as in `ANF-090`. The large padding comb is not claimed to be an exact zero-set packing: only its first spacing is a zero, while (8) controls all higher multiples. The large translation `T_n` is used only to suppress cross energy and does not participate in the conditioning witness. No compactness, asymptotic pair-correlation conjecture, separation theorem, or unproved zeta-zero input is used.

A targeted literature audit covered the current Montgomery--Taylor/Hilbert-space proofs and recent fixed-kernel Gram refinements, together with neighboring nonharmonic-Fourier conditioning literature. Finite-difference loss of conditioning and dilution arguments are classical mechanisms in isolation. No external theorem is load-bearing for (8)--(32), and no source located in that audit states the Mathia-specific combination: a sequence on the exact separable cone with relative Montgomery--Taylor excess tending to zero while both `chi_s` and `chi_s Delta/L` diverge. No new `SOURCES.md` entry is therefore required.

The result does **not** construct a fatal central-notch configuration—indeed (23) says the opposite—and does not show that a properly quotiented condition number can diverge. Its role is to close one tempting repair of `ANF-090`: near-extremality alone cannot rescue the raw ratio. `ANF-091` correctly forces every positive-density subunit chain out of the near-equality regime, but a vanishing-density copy can be hidden inside arbitrarily large near-extremal padding and still dominate the smallest source Gram eigenvalue.

The live all-cardinality gate is consequently sharper. Any useful conditioning invariant must remove exact separable directions **before** taking a worst singular value, or otherwise localize the amplification to the component that actually contributes destination distance. A bound on the unquotiented `a(W)`, on `chi_s(W)`, or even on the product `chi_s(W) Delta(W)/L(W)` cannot close the frontier, including after one assumes Montgomery--Taylor near-extremality.