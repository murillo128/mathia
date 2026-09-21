# WI-384 — Prime-power source sparsity removes the fixed-scale perforation uncertainty

**Status:** `EXACT-DERIVED + CLASSICAL-ARITHMETIC + PRIMARY-SOURCE-OPERATOR-AUDIT + DECISIVE-ROUTE-REDIRECTION + PRIOR-ART-AUDITED + NON-ESTABLISHED-RH`.

## Claim

WI-382 transferred the source-perforated WI-381 arithmetic-plus-polar layer to the fixed-profile Chebyshev remainder only up to an `O_L(1)` error,

\[
Q_k^{\rm arith}+Q_k^{\rm pol}=R_L(x_k)+O_L(1),
\qquad x_k=k+1,
\tag{1}
\]

and WI-383 therefore left that order-one transfer term as the only possible direct-repair carrier inside the fixed-width trial family. That uncertainty is not genuine. The source set contains prime-power slots, not arbitrary integer slots, and the sharper prime-power count already used in WI-377 improves the fixed-window perforation measure by a factor `1/\log x_k`.

Fix `L>0` and retain the WI-381/WI-382 definitions

\[
g(s)=\sqrt{\frac2L}\cos\!\left(\frac{\pi s}{L}\right)
\mathbf 1_{|s|\le L/2},
\qquad
q=g*g,
\tag{2}
\]

\[
Q(z)=\int_{-L}^{L}q(t)e^{zt}\,dt,
\tag{3}
\]

and

\[
R_L(x)=
2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
q\!\left(\log\frac n x\right)
-2Q(1/2)\sqrt x.
\tag{4}
\]

Let `p_k` be the actual centered source-perforated positive lobe from WI-380/WI-381 and `q_k=p_k*p_k`. Then the fixed-width source holes satisfy

\[
\boxed{
|S_k\cap I_k|
=O_L\!\left(\frac1{\sqrt{x_k}\log x_k}\right),
}
\tag{5}
\]

and consequently

\[
\boxed{
\|p_k-g\|_1+
\|q_k-q\|_\infty
=O_L\!\left(\frac1{\sqrt{x_k}\log x_k}\right).
}
\tag{6}
\]

The resulting source-dependent error in the critical arithmetic term and in the leading polar term is therefore only `O_L(1/\log x_k)=o(1)`, not `O_L(1)`.

More precisely, the full arithmetic-plus-polar layer has the exact asymptotic

\[
\boxed{
Q_k^{\rm arith}+Q_k^{\rm pol}
=R_L(x_k)+C_L+O_L\!\left(\frac1{\log x_k}\right),
}
\tag{7}
\]

where the stationary constant is

\[
\boxed{
C_L=
4Q(1/2)
-4\sum_{2\le n<e^L}
\frac{\Lambda(n)}{\sqrt n}q(\log n)
=-2R_L(1).
}
\tag{8}
\]

Thus

\[
\boxed{
Q_k^{\rm arith}+Q_k^{\rm pol}
=R_L(x_k)-2R_L(1)+O_L\!\left(\frac1{\log x_k}\right).
}
\tag{9}
\]

The formerly uncontrolled order-one term in WI-382/WI-383 therefore collapses to an explicit, `k`-independent constant plus a vanishing error. **The source perforation itself does not provide a moving order-one repair reserve at fixed width.**

Combining (9) with WI-383 gives a sharper unconditional dichotomy. If RH is false,

\[
\liminf_{k\to\infty}
\left(Q_k^{\rm arith}+Q_k^{\rm pol}\right)
=-\infty.
\tag{10}
\]

If RH is true, with WI-383's

\[
A_L=4\sum_{\gamma>0}m_\gamma Q(i\gamma)>0,
\]

one has

\[
\boxed{
\liminf_{k\to\infty}
\left(Q_k^{\rm arith}+Q_k^{\rm pol}\right)
=-A_L-2R_L(1).
}
\tag{11}
\]

No sign is asserted for the finite scalar `-A_L-2R_L(1)`. The result does not by itself rule out fixed-scale arithmetic repair; it reduces the entire asymptotic arithmetic-plus-polar question for this trial family to one explicit scalar comparison under RH, while removing source perforation as an independent order-one carrier.

## 1. Prime-power sparsity sharpens the fixed-window hole measure

The WI-377/Desogus source set is

\[
S_k=
\bigcup_{\substack{2\le n\le k\\ \Lambda(n)>0}}
J_{k,n},
\qquad
J_{k,n}=
[\log k-\log n,\,\log(k+1)-\log n),
\tag{12}
\]

and every slot has the same width

\[
\varepsilon_k
=\log\!\left(1+\frac1k\right)
=O(x_k^{-1}).
\tag{13}
\]

The fixed-width positive lobe is supported on

\[
I_k=
\left[
\frac{\log x_k-L}{2},
\frac{\log x_k+L}{2}
\right].
\tag{14}
\]

If `J_{k,n}` meets `I_k`, its right endpoint exceeds the left endpoint of (14), so

\[
\log x_k-\log n>
\frac{\log x_k-L}{2},
\]

hence

\[
 n<e^{L/2}\sqrt{x_k}.
\tag{15}
\]

WI-380 bounded the number of such slots by the number of all integers below the right side of (15), obtaining `O_L(\sqrt{x_k})`. But only `n` with `\Lambda(n)>0` occur. The classical prime-power count gives

\[
\#\{n\le Y:\Lambda(n)>0\}
=O\!\left(\frac{Y}{\log Y}\right).
\tag{16}
\]

Indeed the primes contribute `O(Y/\log Y)` by Chebyshev, while prime powers of exponent at least two contribute `O(\sqrt Y\log Y)`, which is smaller for large `Y`.

Taking `Y=e^{L/2}\sqrt{x_k}` in (16), the number `M_k` of relevant source slots is therefore

\[
M_k
=O_L\!\left(\frac{\sqrt{x_k}}{\log x_k}\right).
\tag{17}
\]

Multiplying by the common width (13) gives (5):

\[
|S_k\cap I_k|
\le M_k\varepsilon_k
=O_L\!\left(\frac1{\sqrt{x_k}\log x_k}\right).
\tag{18}
\]

Overlaps only improve this upper bound. The same estimate survives the fixed-multiple slot enlargement used when one replaces the indicator cutoff by a smooth form-core cutoff.

This is not a new prime-power estimate. It is exactly the sparsity mechanism already used on macroscopic interiors in WI-377, now applied to the fixed centered window where WI-380/WI-382 had retained the cruder all-integer count.

## 2. The source-dependent kernel error is `o(x_k^{-1/2})`

In centered coordinates the WI-380 construction has

\[
p_k=\chi_k g,
\qquad 0\le\chi_k\le1,
\tag{19}
\]

with `1-\chi_k` supported on the source holes, or on a fixed-multiple enlargement of them in the smooth cutoff variant. Since `g` is bounded on fixed support, (18) gives

\[
\boxed{
\|p_k-g\|_1
=O_L\!\left(\frac1{\sqrt{x_k}\log x_k}\right).
}
\tag{20}
\]

Also `\|p_k\|_\infty\le\|g\|_\infty`. With `q_k=p_k*p_k`,

\[
q_k-q
=(p_k-g)*p_k+g*(p_k-g),
\]

so the `L^1*L^\infty\to L^\infty` Young inequality yields

\[
\boxed{
\|q_k-q\|_\infty
=O_L\!\left(\frac1{\sqrt{x_k}\log x_k}\right).
}
\tag{21}
\]

This is the quantitative improvement over WI-382 equation (30), whose `O_L(x_k^{-1/2})` rate was just large enough to leave an order-one arithmetic transfer error.

## 3. The critical arithmetic profile replacement now costs `o(1)`

WI-381 gives the exact favorable cross-lobe contribution

\[
Q_k^{\rm crit}
=2\sum_n
\frac{\Lambda(n)}{\sqrt n}
q_k\!\left(\log\frac n{x_k}\right),
\tag{22}
\]

with support restricted to

\[
x_ke^{-L}\le n\le x_ke^L.
\]

Chebyshev's estimate `\psi(y)=O(y)` and partial summation give

\[
\sum_{x_ke^{-L}\le n\le x_ke^L}
\frac{\Lambda(n)}{\sqrt n}
=O_L(\sqrt{x_k}).
\tag{23}
\]

Combining (21) and (23),

\[
\boxed{
Q_k^{\rm crit}
=
2\sum_n\frac{\Lambda(n)}{\sqrt n}
q\!\left(\log\frac n{x_k}\right)
+O_L\!\left(\frac1{\log x_k}\right).
}
\tag{24}
\]

By definition (4), the fixed-profile sum in (24) equals

\[
R_L(x_k)+2Q(1/2)\sqrt{x_k}.
\tag{25}
\]

Thus the exact source holes perturb the critical arithmetic remainder by a vanishing amount.

## 4. The leading polar replacement also costs `o(1)`

Retain WI-381's notation

\[
I_{k,+}=\int e^{s/2}p_k(s)\,ds,
\qquad
I_{k,-}=\int e^{-s/2}p_k(s)\,ds,
\tag{26}
\]

and let

\[
I_+=\int e^{s/2}g(s)\,ds,
\qquad
I_-=\int e^{-s/2}g(s)\,ds.
\tag{27}
\]

On the fixed support, (20) implies

\[
I_{k,\pm}-I_\pm
=O_L\!\left(\frac1{\sqrt{x_k}\log x_k}\right).
\tag{28}
\]

Consequently

\[
\sqrt{x_k}
\left(I_{k,+}^2-I_+^2\right)
=O_L\!\left(\frac1{\log x_k}\right).
\tag{29}
\]

The exact polar term from WI-381 is

\[
Q_k^{\rm pol}
=-2\sqrt{x_k}I_{k,+}^2
+4I_{k,+}I_{k,-}
-2x_k^{-1/2}I_{k,-}^2.
\tag{30}
\]

Because `g` is even,

\[
I_+=I_-,
\qquad
I_+^2
=\int e^{t/2}q(t)\,dt
=Q(1/2).
\tag{31}
\]

Equations (28)--(31) therefore give

\[
\boxed{
Q_k^{\rm pol}
=-2Q(1/2)\sqrt{x_k}
+4Q(1/2)
+O_L\!\left(\frac1{\log x_k}\right).
}
\tag{32}
\]

The final term `-2x_k^{-1/2}I_{k,-}^2` is actually `O_L(x_k^{-1/2})` and is absorbed by the displayed error.

Combining (24), (25), and (32) already yields

\[
Q_k^{\rm crit}+Q_k^{\rm pol}
=R_L(x_k)+4Q(1/2)
+O_L\!\left(\frac1{\log x_k}\right).
\tag{33}
\]

## 5. The same-lobe term converges to an explicit finite constant

The only remaining arithmetic contribution comes from fixed shifts

\[
0<\log n<L,
\]

so only the finite set `2\le n<e^L` occurs. Let

\[
a_{p_k}(h)=\int p_k(s+h)p_k(s)\,ds
\tag{34}
\]

be the positive-lobe autocorrelation. For each fixed `|h|<L`, boundedness of `p_k,g` and (20) give

\[
a_{p_k}(h)=a_g(h)
+O_L\!\left(\frac1{\sqrt{x_k}\log x_k}\right).
\tag{35}
\]

Since `g` is even,

\[
a_g(h)=q(h).
\tag{36}
\]

The odd full trial has two identical same-lobe overlaps at a small positive shift, so its full autocorrelation is `2a_{p_k}(h)`. The arithmetic coefficient is `-2\Lambda(n)/\sqrt n`. Therefore

\[
\boxed{
Q_k^{\rm small}
=
-4\sum_{2\le n<e^L}
\frac{\Lambda(n)}{\sqrt n}q(\log n)
+O_L\!\left(\frac1{\sqrt{x_k}\log x_k}\right).
}
\tag{37}
\]

The endpoint `n=e^L`, if it happens to be an integer prime power, is immaterial because `q(L)=0`.

Adding (33) and (37) proves (7)--(8). Finally, evaluating the definition (4) at `x=1` gives

\[
R_L(1)
=
2\sum_{2\le n<e^L}
\frac{\Lambda(n)}{\sqrt n}q(\log n)
-2Q(1/2),
\tag{38}
\]

so indeed `C_L=-2R_L(1)`, proving (9).

## 6. Consequence for the WI-383 recurrence barrier

WI-383 proves the unconditional alternative

\[
\neg\mathrm{RH}
\Longrightarrow
\liminf_{k\to\infty}R_L(x_k)=-\infty,
\tag{39}
\]

while under RH

\[
\liminf_{k\to\infty}R_L(x_k)=-A_L.
\tag{40}
\]

Since the error in (9) tends to zero, (39)--(40) transfer without any unknown bounded perturbation and give (10)--(11).

This materially sharpens the route diagnosis from WI-383. The unresolved `O_L(1)` in WI-382 was not hiding an arbitrary `k`-dependent source-perforation correction. At fixed width, prime-power sparsity forces that moving correction to vanish. What remains in the arithmetic-plus-polar layer is the recurrent Chebyshev remainder plus the explicit stationary scalar `-2R_L(1)`.

The sign question is therefore finite and concrete under RH:

\[
-A_L-2R_L(1)
\tag{41}
\]

is the exact asymptotic lower floor of this arithmetic-plus-polar layer. A proof that (41) is negative would close direct fixed-scale repair for this trial family; a proof that it is positive would exhibit a genuine stationary reserve. This finding establishes neither sign.

The other branch from WI-382/WI-383 also remains live: the rooted graph/domain relation could exclude these source-zero gamma-negative trials before this old--old arithmetic-plus-polar form is evaluated. Equation (9) concerns only the arithmetic-plus-polar layer once the trial is admitted.

## 7. Prior-art and novelty audit

The arithmetic estimate (16) is classical and is already part of Mathia's established evidence in WI-377. Chebyshev's estimate and partial summation in (23) are likewise classical. The exact source slots and rooted arithmetic/polar normalizations come from Marco Desogus, *The Three Gates: A Rooted-Operator Approach to Weil Positivity*, arXiv:2609.20367v1 (17 Sep 2026); none of that preprint's claimed RH conclusion is used.

The nearby literature audited for WI-382/WI-383 covers Landau--Pintz oscillation, smooth weighted prime remainders, and almost-periodic explicit-formula recurrence. A fresh targeted search around source perforations, fixed logarithmic windows, prime-power slot sparsity, and smoothed Chebyshev remainders did not locate the specific sharpening (5)--(9). The ingredients are not new: the Mathia-specific deduction is that the **actual prime-power density of the Desogus source slots eliminates the entire moving order-one transfer uncertainty left by WI-382**. No priority claim is made.

No new external source is needed beyond the sources already anchored by WI-377 and WI-382/WI-383, so `SOURCES.md` is intentionally unchanged.

## 8. Boundaries and falsification

- Fixed `L` is essential. If `L=L(k)` grows, both the number of source slots and the weighted critical-annulus mass change, and the `O(1/\log x_k)` transfer does not follow from this argument.
- The result concerns the WI-380/WI-381 source-perforated **arithmetic-plus-polar layer**. It does not bound an independent rooted-domain, Schur-complement, graph, or operator correction outside that layer.
- Equation (9) does not assert a sign for `-2R_L(1)` or for the RH floor `-A_L-2R_L(1)`. A stationary positive constant could still offset the recurrent zero sum.
- No Riemann-hypothesis conclusion is used or claimed. RH appears only in the second branch of the WI-383 dichotomy used to identify the exact finite floor.
- The rate (5) uses that the source set is indexed by `\Lambda(n)>0`, hence by prime powers. Replacing the source set by all integers would restore the older `O_L(x_k^{-1/2})` scale and the present sharpening would fail.
- The small-shift constant (37) uses the exact odd two-lobe geometry of the WI-380 trial. A different trial geometry must re-evaluate that finite term.

The next high-value test is now sharply finite: evaluate or bound the scalar comparison `-A_L-2R_L(1)` for the admissible `L=L_\eta`, or prove that the rooted graph/domain relation excludes the corresponding trial. Further bookkeeping of source perforations at fixed width cannot produce an independent order-one rescue term.