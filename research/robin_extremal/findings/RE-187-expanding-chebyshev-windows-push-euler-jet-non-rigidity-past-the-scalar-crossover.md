# RE-187 — Expanding Chebyshev windows push Euler-jet non-rigidity past the scalar crossover

**Status:** `EXACT-DERIVED + CONSTRUCTIVE-CONTROL + ORDINARY-PRIME-SUPPORT + MULTIPLICITY-012 + GROWING-EULER-JET-MATCHING + EXPANDING-CHEBYSHEV-WINDOWS + MICROSTEPPED-SHELL-PACKING + KV-FIDELITY + TRANSIENT-ROBIN-AMBIGUITY + RE-186-STRENGTHENING + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-173, RE-178, RE-186.

`RE-186` shows that exact ordinary-prime `{0,1,2}` controls can match every boundary Euler jet through

\[
K=o\!\left(\frac{\log p}{\log\log p}\right)
\]

while preserving every fixed Korobov--Vinogradov fidelity envelope and an order-one transient Robin excursion. Its apparent boundary comes from fixing the logarithmic Chebyshev interpolation width to `W=1`; the exact prime-power remainder is then bounded by `exp(-L+O(K log L))` at baseline `L\asymp\log p`.

That boundary is not intrinsic. The centered Euler kernels admit an exact prime-power resummation in the Chebyshev coordinate, and the interpolation window can widen with `p`. Widening the window lowers the normalized prime-power displacement while the microstep residue construction of `RE-186` still keeps every ordinary-prime shell globally disjoint.

Let

\[
L_p:=\log(16p),
\qquad
K=K(p),
\]

and assume

\[
\boxed{
K=o\!\left((\log p)^{4/3}(\log\log p)^{1/6}\right).
}
\tag{1}
\]

Set

\[
\boxed{
W_p:=\max\left\{1,\frac{64K^2}{L_p}\right\}.
}
\tag{2}
\]

Then for every sufficiently large selector prime `p` there exists an ordinary-prime-supported source `Q_{p,K}` with

\[
\boxed{m_{Q_{p,K}}(q)\in\{0,1,2\}}
\tag{3}
\]

such that:

1. `Q_{p,K}` agrees with the ordinary prime source below `2p`;
2. it contains the canonical `RE-173` deletion packet `D_p\subset[2p,3p]` and has no repair below `16p`;
3. writing
   \[
   D_Q(s):=\sum_q(m_Q(q)-1)[-\log(1-q^{-s})],
   \]
   every boundary derivative through depth `K` matches exactly,
   \[
   \boxed{D_Q^{(j)}(1+)=0,\qquad 0\le j\le K;}
   \tag{4}
   \]
4. the correction series is absolutely convergent in every derivative in (4);
5. for every fixed `b>0`,
   \[
   \boxed{
   |\vartheta_Q(X)-\vartheta(X)|\ll_b X e^{-bV(X)}
   \qquad(X\ge2p),
   }
   \tag{5}
   \]
   once `p` is sufficiently large, where
   \[
   V(X)=\frac{(\log X)^{3/5}}{(\log\log X)^{1/5}};
   \]
6. before repair is visible, the canonical Robin coordinate still has an order-one excursion,
   \[
   \boxed{
   \mathcal A_{p,8p}(Q_{p,K})-
   \mathcal A_{p,8p}(P)\asymp1.
   }
   \tag{6}
   \]

Thus the scalar crossover `log p/log log p` isolated in `RE-178` is not a source-rigidity threshold. Exact matched non-rigidity survives parametrically beyond it, through every depth satisfying (1). The price is spatial rather than algebraic: the repair reservoir must spread over a growing logarithmic window of width `W_p\asymp K^2/\log p` once `K\gg\sqrt{\log p}`.

## 1. Exact resummation exposes the real prime-power geometry

Retain the positive Euler kernels from `RE-186`,

\[
H(q):=\log\frac q{q-1},
\qquad
U_j(q):=(\log q)^j\sum_{n\ge1}n^{j-1}q^{-n}
\quad(j\ge1),
\qquad U_0=H,
\]

and the centered kernels at baseline `x=e^L`,

\[
C_{j,L}(q)
:=
\sum_{r=0}^j\binom jr(-L)^{j-r}U_r(q).
\tag{7}
\]

The definition can be resummed **exactly** before any large-`q` approximation:

\[
\boxed{
C_{j,L}(q)
=
\sum_{n\ge1}\frac{q^{-n}}n
(n\log q-L)^j.
}
\tag{8}
\]

For a window width `W>0`, define

\[
P_{m,W}(t):=T_m\!\left(\frac{2t}{W}-1\right),
\qquad
P_{m,W}(t)=\sum_{j=0}^m a_{mj}^{(W)}t^j,
\]

and

\[
\Psi_{m,L,W}(q)
:=
\sum_{j=0}^m a_{mj}^{(W)}C_{j,L}(q).
\tag{9}
\]

Equation (8) gives the exact identity

\[
\boxed{
\Psi_{m,L,W}(q)
=
\sum_{n\ge1}\frac{q^{-n}}n
P_{m,W}(n\log q-L).
}
\tag{10}
\]

If `q=e^{L+\alpha}` with `0\le\alpha\le W`, the `n=1` term is exactly

\[
q^{-1}P_{m,W}(\alpha),
\]

and `|P_{m,W}(\alpha)|\le1`. Thus the only deviation from the ideal Chebyshev response comes from the genuine prime powers `n\ge2`; no coefficientwise monomial estimate is needed.

## 2. A width `W\gg K^2/L` makes every prime-power mode exponentially harmless

For `v\ge0`,

\[
\boxed{
|T_m(2v-1)|\le e^{2m\sqrt v}.
}
\tag{11}
\]

For `0\le v\le1` this is trivial from `|T_m|\le1`. For `v\ge1`, it follows from

\[
T_m(2v-1)=\cosh(m\operatorname{arcosh}(2v-1))
\]

and `\operatorname{arcosh}(2v-1)\le2\sqrt v`.

Divide (10) by `H(q)\ge q^{-1}`. For the `n`-th prime-power term put

\[
v:=\frac{(n-1)L+n\alpha}{W}.
\]

Since

\[
(n-1)(L+\alpha)
=W\bigl(v-\alpha/W\bigr)
\ge \frac W2v
\qquad(n\ge2),
\tag{12}
\]

(11) gives, uniformly for `m\le K`,

\[
q^{1-n}|P_{m,W}(n\log q-L)|
\le
\exp\!\left(-\frac W2v+2K\sqrt v\right).
\tag{13}
\]

The exponent in (13) is decreasing for `v\ge L/W` whenever

\[
W\ge\frac{4K^2}{L}.
\]

With the stronger convenient choice

\[
W\ge\frac{64K^2}{L},
\tag{14}
\]

and `v\ge(n-1)L/W`, one obtains

\[
-\frac W2v+2K\sqrt v
\le
-\frac{(n-1)L}{4}.
\tag{15}
\]

The subtraction caused by the denominator `H(q)` contributes only another bounded copy of the same geometric tail. Therefore

\[
\boxed{
\max_{m\le K}
\left|
\frac{\Psi_{m,L,W}(q)}{H(q)}
-P_{m,W}(\alpha)
\right|
\ll e^{-L/4}
}
\tag{16}
\]

uniformly for `0\le\alpha\le W`.

This is the decisive improvement over `RE-186`. The prime-power error no longer has the form `exp(-L+O(K log L))`. Once the window pays `W\asymp K^2/L`, the whole prime-power stack is exponentially negligible **independently of the size of `K`** within the remaining source-placement budget.

## 3. Expanding Chebyshev tracks remain globally disjoint

Use the same microstep scale as `RE-186`,

\[
h:=e^{-a_0V(p)/8},
\qquad
x_n:=16p\,e^{nh},
\qquad n\ge0,
\tag{17}
\]

where `a_0>0` is supplied by the anchored KV prime number theorem. Keep a relative prime-shell width

\[
\delta_n:=e^{-a_0V(x_n)/4}.
\tag{18}
\]

For the width `W=W_p`, start from the scaled Gauss--Chebyshev nodes

\[
\bar\alpha_r
:=
\frac W2\left(1+\cos\frac{(2r+1)\pi}{2(K+1)}\right),
\qquad0\le r\le K.
\tag{19}
\]

Their smallest spacing and endpoint distance are `\asymp W/K^2`. By (2),

\[
\frac W{K^2}\gg\frac1{L_p},
\tag{20}
\]

while `h` is smaller than every negative power of `L_p`. Hence each node may be perturbed by at most `h` so that

\[
\alpha_r\equiv\frac{rh}{K+1}\pmod h.
\tag{21}
\]

Put the `r`-th shell of generation `n` around

\[
y_{n,r}:=x_ne^{\alpha_r}.
\tag{22}
\]

Exactly as in `RE-186`, distinct pairs `(n,r)` have logarithmic center separation at least `h/(K+1)`. Since

\[
\delta_n\le h^2=o(h/K),
\tag{23}
\]

all shells from all generations are pairwise disjoint. Every ordinary prime is therefore edited at most once, and multiplicities remain in `{0,1,2}`.

The KV PNT is more than sufficient for the wider shells. A shell centered at `y_{n,r}\ge x_n` has weighted supply

\[
\sum_{q\in I_{n,r}}H(q)
\asymp
\frac{\delta_n}{\log y_{n,r}},
\tag{24}
\]

because the PNT error at `y_{n,r}` is no larger than at `x_n`, whereas the chosen relative width is `e^{-a_0V(x_n)/4}`. Under (1), all polynomial factors in `K`, `L_p`, and `W_p` are negligible compared with this supply at the stages where nontrivial mass is requested.

## 4. The shell matrix remains DCT-conditioned

At the ideal nodes,

\[
P_{m,W}(\bar\alpha_r)
=
\cos\frac{m(2r+1)\pi}{2(K+1)},
\]

so the ideal matrix is exactly the same discrete-cosine matrix used by `RE-185`--`RE-186`, with

\[
\|A_K^{-1}\|_{\infty\to1}\ll K.
\tag{25}
\]

Scaling the interval actually reduces geometric sensitivity:

\[
\left|\frac d{d\alpha}P_{m,W}(\alpha)\right|
\ll\frac{m^2}{W}.
\tag{26}
\]

Thus node perturbation and within-shell variation contribute at most

\[
O\!\left(\frac{K^2(h+\delta_n)}W\right)
\]

per entry, while (16) contributes `O(e^{-L_n/4})`, `L_n=\log x_n`. Because `W_p\ge64K^2/L_p` and hence also `W_p\ge64K^2/L_n` is **not** needed—the inequality required in (14) becomes easier as `L_n` grows, since `64K^2/L_n\le64K^2/L_p\le W_p`—the prime-power estimate holds uniformly at every later generation.

Consequently the exact shell matrices satisfy, for all sufficiently large `p`,

\[
\boxed{
\|A_n^{-1}\|_{\infty\to1}\ll K
}
\tag{27}
\]

uniformly in `n`.

## 5. Microstep recentering is even cheaper on the wide window

Moving the baseline from `L` to `L+h` translates the normalized Chebyshev variable by only `2h/W`. The standard exterior growth estimate therefore gives

\[
\|\mathcal T_{h,W}\|_{\infty\to\infty}
\ll
K\exp\!\left(CK\sqrt{h/W}\right).
\tag{28}
\]

Under (1), `K` is only a power of `\log p` up to a slowly varying factor, whereas `h` is exponentially small in `V(p)`. Hence

\[
K\sqrt{h/W}=o(1),
\]

and (28) is `O(K)` exactly as needed in the `RE-186` contraction argument.

Let `M_n` denote the exact `\ell^\infty` residual in the `K+1` scaled Chebyshev coordinates at baseline `L_n`. Solving the real shell system, quantizing each signed `H`-mass by distinct ordinary primes, and recentering gives the same schematic recurrence

\[
M_{n+1}
\le
\frac13M_n
+O\!\left(\frac{K^2}{x_n}\right)
\tag{29}
\]

for all sufficiently large `p`. The contraction follows from (23), (26), (27), (28), and the exponentially small exact prime-power error (16).

The initial deletion packet lies a fixed logarithmic distance to the **left** of the first repair baseline. In the scaled variable this is only `O(1/W)` beyond the endpoint. The same Chebyshev exterior formula gives

\[
M_0
\le
\exp\!\left(O\!\left(\frac K{\sqrt W}\right)\right)d_p,
\qquad
 d_p\asymp\frac1{\sqrt p\log p}.
\tag{30}
\]

With (2), either `W=1` and `K=O(\sqrt{L_p})`, or

\[
\frac K{\sqrt W}\ll\sqrt{L_p}.
\]

Thus

\[
\boxed{M_0=p^{-1/2+o(1)}.}
\tag{31}
\]

The first-generation requested `H`-mass is still only `p^{-1/2+o(1)}`, far below the supply (24). Iterating (29) drives `M_n` to zero and gives absolute convergence in every raw derivative order `j\le K`. Since `K` is finite for each fixed `p`, the triangular change of coordinates between the scaled Chebyshev frame and the raw Euler jets is exact; letting `n\to\infty` proves (4).

## 6. The new depth is paid for by support radius, not by loss of KV fidelity

The wider window means that the first repair generation can reach logarithmic height

\[
L_p+W_p.
\]

This is the only genuinely new source-fidelity issue. Condition (1) is exactly strong enough to keep that placement well inside every fixed KV horizon.

Indeed, from (1)--(2),

\[
W_p
=o\!\left(
L_p^{5/3}(\log L_p)^{1/3}
\right),
\tag{32}
\]

and therefore

\[
\boxed{
V\!\left(e^{L_p+W_p}\right)=o(L_p).
}
\tag{33}
\]

For the early generations, the total requested `H`-mass is `p^{-1/2+o(1)}` by (29)--(31). Up to any cutoff inside their support, the corresponding Chebyshev discrepancy is therefore at most

\[
X\,p^{-1/2+o(1)}.
\tag{34}
\]

Equation (33) implies that for every fixed `b>0`,

\[
p^{-1/2+o(1)}=o\!\left(e^{-bV(X)}\right)
\]

throughout this initial expanded reservoir.

After the initial reservoir has been passed, its completed discrepancy is fixed while `X e^{-bV(X)}` is eventually increasing. The geometric part of (29) has by then decayed super-exponentially in logarithmic distance because one generation occurs every `h` units, and the rounding floor contributes at most

\[
e^{W_p}p^{o(1)}(1+\log X)^2
\tag{35}
\]

up to cutoff `X`. At the end of the initial reservoir the right side of the KV envelope has an extra factor `e^{L_p}` over (35), modulo `e^{o(L_p)}` by (33), and the margin only improves afterwards. This proves (5).

The stronger global selector-scale discrepancy estimate of `RE-186`,

\[
|\vartheta_Q(X)-\vartheta(X)|
\le p^{1/2+o(1)}+p^{o(1)}(1+\log X)^2,
\]

is **not** retained: expanding the repair window deliberately allows larger absolute discrepancies at much larger `X`. What is retained is the source-level property that matters for the matched-control test—every fixed KV relative envelope.

## 7. The scalar crossover was a fixed-window artifact

At the old width `W=1`, controlling prime powers asks roughly for

\[
K\log\log p=o(\log p),
\]

which happens to meet the scalar leverage crossover in `RE-178`. The exact identity (10) shows that these are distinct mechanisms. The prime-power tail cares about the **normalized displacement** of a prime power from the interpolation window, while the scalar capacity calculation cares about powers of the remote logarithmic location.

Choosing

\[
W\asymp\frac{K^2}{\log p}
\]

balances the Chebyshev exterior growth against the `q^{-n}` suppression and replaces the fixed-window depth restriction by the placement restriction (33). Solving that placement condition yields precisely the scale (1):

\[
K=o\!\left((\log p)^{4/3}(\log\log p)^{1/6}\right).
\]

In particular,

\[
\frac{K}{\log p/\log\log p}\to\infty
\]

is allowed. So the first polynomial leverage of high scalar jets does not by itself create rigidity; a source-faithful repair can pay for those jets by using a broader but still KV-invisible prime reservoir.

## 8. Representation audit

The generic layer is approximation geometry. Equation (10) is simply exact resummation of a polynomial basis against an exponential series; (11) is elementary Chebyshev exterior growth; the DCT conditioning and residue-separated microstep tracks are the same classical devices already isolated in `RE-185`--`RE-186`.

The source-specific layer is the simultaneous compatibility of four constraints: exact Euler prime-power kernels, ordinary-prime quantization with one-copy deletion/duplication, unconditional KV prime supply in every chosen shell, and the requirement that the entire enlarged support remain invisible to every fixed KV fidelity envelope at the selector debt scale `d_p\asymp(\sqrt p\log p)^{-1}`. The exponent `4/3` in (1) comes from coupling the Chebyshev width tariff `W\asymp K^2/L` to the KV invisibility condition `V(e^W)=o(L)`; it is not a generic Chebyshev exponent.

This remains a matched-control non-rigidity theorem. It does not make the boundary jets source-native for Robin, and it does not weaken the full-germ identification result `RE-174`. It says that even a jet stack parametrically deeper than the scalar crossover can be reproduced by an honest prime-supported bounded-multiplicity control without exposing itself at any fixed KV scale.

## 9. Adversarial self-review

The first possible overclaim is that (16) might hide coefficient growth from converting monomials to Chebyshev polynomials. Equation (10) removes that issue: the polynomial is evaluated **after** exact resummation of each prime-power mode, so no coefficientwise `C^K(\log q)^K` loss is inserted.

The second is shell collision when `W` grows. The scaled Chebyshev spacing is `\asymp W/K^2\gg1/L_p`, while the residue perturbation is only `h` and the shell width is `O(h^2)`. The global congruence argument is therefore stronger, not weaker, than in `RE-186`.

The third is insufficient prime supply at far-right nodes. The requested object is `H`-mass, and a relative PNT shell around `y` supplies `\asymp\delta/\log y`; the dependence on `y` cancels to first order because each prime contributes `H(q)\asymp1/y`. The polynomial growth of `\log y\le L_n+W_p` is negligible compared with the PNT shell margin in the relevant stages.

The fourth is loss of source fidelity from far placement. This is the real tariff and is why (1) stops at the stated scale. The initial debt is `p^{-1/2+o(1)}` in `H`-mass. To hide it from **every fixed** KV envelope at a shell of logarithmic height `L_p+W_p`, one needs `V(e^{L_p+W_p})=o(L_p)`, not merely `O(L_p)`. Equation (33) is exactly that requirement.

Finally, (1) is a sufficient range, not a sharp barrier. A different polynomial frame, a nonuniform window, or a position-dependent allocation of high modes may reduce the quadratic width tariff `K^2/L`; conversely, a rigidity theorem would need a lower bound showing that some comparable spatial tariff is unavoidable. No such lower bound is proved here.

## 10. Prior-art audit

The external search boundary remains the same broad neighborhood as `RE-186`: Beurling/generalized-prime constructions, perturbations of generalized Euler products, Chebyshev interpolation, and modern KV-type PNT estimates. Recent Beurling-prime work shows substantial flexibility of generalized prime systems and zeta functions, but it does not provide the ordinary-prime `{0,1,2}` shell quantization, exact growing boundary-jet matching, or transient Robin excursion used here.

No new external theorem is load-bearing. The only arithmetic supply estimate is the KV prime number theorem already anchored in `research/robin_extremal/SOURCES.md`; the new step is the exact identity (10) and the elementary estimate (11)--(16). Therefore `SOURCES.md` needs no change.

## Conclusion

The coincidence in `RE-186` between the fixed-width prime-power error and the scalar capacity crossover was accidental. Exact prime-power resummation shows that high Euler modes can be made cheap by enlarging the interpolation window, while microstepped residue tracks keep the resulting ordinary-prime edits disjoint.

Consequently exact source-faithful matched non-rigidity extends from

\[
K=o\!\left(\frac{\log p}{\log\log p}\right)
\]

to the parametrically larger range

\[
\boxed{
K=o\!\left((\log p)^{4/3}(\log\log p)^{1/6}\right).
}
\]

The live scalar frontier is therefore no longer the first high-jet capacity crossover. The next genuine question is whether the quadratic spatial tariff `W\asymp K^2/\log p` is intrinsic, or whether a more adaptive joint representation can push exact matched controls deeper before the fixed-KV invisibility budget itself becomes the obstruction.