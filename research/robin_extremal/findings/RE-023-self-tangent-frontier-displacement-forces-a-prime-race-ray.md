# RE-023 — self-tangent frontier displacement forces a prime-race ray

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + UNIVERSAL-SELF-TANGENT-DISPLACEMENT-LAW + SUB-SQUARE-ROOT-ENVELOPE-LOCK + COUNTEREXAMPLE-RACE-RAY + SQUARE-ROOT-GAP-DICHOTOMY + PRIOR-ART-BOUNDED`. `RE-021` removes the clean-boundary hypothesis from the self-tangent Robin-height dictionary, while `RE-022` removes it from the finite-annulus localization and records a universal reciprocal-error lower bound for counterexamples. Those results can be coupled more tightly to the actual first-layer selector. The displacement of a self-tangent state from its last active first-layer prime is itself an asymptotic coordinate for the Chebyshev error, and under Robin failure the same displacement shifts the required logarithmic Mertens-product error by the opposite amount.

Let `C` be any sufficiently large regular self-tangent colossally abundant state, put

\[
X:=\log C,
\]

let `p` be its largest active first-layer prime, and define the **frontier displacement**

\[
\boxed{d:=X-p>0.}
\tag{1}
\]

Retain the normalized prime-error coordinates of `RE-009`,

\[
\mathcal E_{\vartheta}(p):=\frac{\vartheta(p)-p}{\sqrt p},
\qquad
\mathcal E_{\pi_\ell}(p)
:=\sqrt p\log p
\left(
\sum_{r\le p}-\log(1-r^{-1})-\gamma-\log\log p
\right).
\tag{2}
\]

Put

\[
L_p:=\log p,
\qquad
\ell_p:=\frac12W(2pL_p).
\tag{3}
\]

Then for every fixed `M>0`, uniformly over regular self-tangent states,

\[
\boxed{
\mathcal E_{\vartheta}(p)
=
\frac d{\sqrt p}
-
\sqrt{\frac{L_p}{\ell_p}}
+O_M(L_p^{-M}).
}
\tag{4}
\]

In particular,

\[
\boxed{
\mathcal E_{\vartheta}(p)
=
\frac d{\sqrt p}
-\sqrt2
+
\frac{\sqrt2\log2}{2\log p}
+O((\log p)^{-2}).
}
\tag{5}
\]

If `C` is moreover a Robin counterexample, then the exact Euler-product height factorization and the universal exponent-tail asymptotics imply

\[
\boxed{
\mathcal E_{\pi_\ell}(p)
-
\frac d{\sqrt p}
\ge
\sqrt2-O((\log p)^{-1}).
}
\tag{6}
\]

Thus the selector does not merely demand the mixed difference `mathcal E_(pi_l)-mathcal E_vartheta` to cross the `2sqrt(2)` threshold of `RE-021`. It places a hypothetical counterexample asymptotically on a one-parameter family of joint race corners indexed by `d/sqrt(p)`. Along any unbounded counterexample subsequence for which

\[
\frac d{\sqrt p}\longrightarrow\delta\in[0,\infty),
\tag{7}
\]

one necessarily has

\[
\boxed{
\mathcal E_{\vartheta}(p)\longrightarrow\delta-\sqrt2,
\qquad
\liminf\mathcal E_{\pi_\ell}(p)\ge\delta+\sqrt2.
}
\tag{8}
\]

If `d/sqrt(p) -> +infinity`, equations (4) and (6) instead force both normalized coordinates to `+infinity` after subtracting their respective fixed `sqrt(2)` offsets. The square-root displacement is therefore the precise scale at which the selected joint race changes chamber.

For a regular self-tangent **local peak**, let `u<v` be the consecutive ordinary-prime envelope from `RE-017` and let

\[
g:=v-u.
\]

The first-layer frontier is `p=u`, and the event geometry gives exactly

\[
\boxed{0<d<g+1.}
\tag{9}
\]

Consequently every counterexample-peak sequence with

\[
g=o(\sqrt p)
\tag{10}
\]

falls into the same joint corner previously obtained in `RE-021` only for fixed envelopes:

\[
\boxed{
\mathcal E_{\vartheta}(p)\to-\sqrt2,
\qquad
\liminf\mathcal E_{\pi_\ell}(p)\ge\sqrt2.
}
\tag{11}
\]

Conversely, if an infinite counterexample-peak sequence escapes this sub-square-root displacement lock, then there is a constant `c>0` and a subsequence with

\[
d\ge c\sqrt p,
\qquad
 g\ge c\sqrt p-1.
\tag{12}
\]

Together with the unconditional `g=O(p^{0.52})` envelope supplied by the current prime-gap input, the purely geometric escape is confined to a square-root-to-`p^0.52` prime-gap chamber. This does not exclude that chamber, but it extends the fixed-envelope joint-race obstruction across every `o(sqrt(p))` ordinary envelope and makes the square-root scale common to both the clean and exceptional transition analyses.

## 1. Self-tangency makes the frontier displacement an exact Chebyshev coordinate

`RE-021` proves that every sufficiently large regular self-tangent state has a canonical last active first-layer prime `p` satisfying

\[
p<X<q+1,
\qquad
X-p=O(p^{0.52}),
\tag{13}
\]

where `q` is the next ordinary prime. It also gives the exact self-tangent layer split

\[
X=\vartheta(p)+\Phi_{\ge2}(X),
\tag{14}
\]

with

\[
\Phi_{\ge2}(X)
:=
\sum_{\substack{r\ \mathrm{prime},\ j\ge2\\ \eta_{r,j}<X}}
\log r.
\]

Subtracting `p` from (14) and using (1) gives the exact identity

\[
\boxed{
\vartheta(p)-p=d-\Phi_{\ge2}(X).
}
\tag{15}
\]

This identity is more informative than the generic statement `|vartheta(p)-p|=O(p^0.52)`: the endpoint error consists of one positive geometric displacement and one deterministic higher-layer mass.

The second-layer analysis of `RE-016`, shown in `RE-021` to survive at every regular self-tangent state, gives for every fixed `M`

\[
\frac{\Phi_{\ge2}(X)}{\sqrt X}
=
\sqrt{\frac{L_X}{\ell_X}}
+O_M(L_X^{-M}),
\qquad
L_X:=\log X,
\quad
\ell_X:=\frac12W(2XL_X).
\tag{16}
\]

Equation (13) implies

\[
\frac Xp=1+O(p^{-0.48}),
\qquad
L_X-L_p=O(p^{-0.48}).
\tag{17}
\]

These errors are smaller than every fixed inverse power of `log p`. Smoothness of the Lambert-`W` expression in (16) therefore allows `X` to be replaced by `p` at the same all-logarithmic precision:

\[
\boxed{
\frac{\Phi_{\ge2}(X)}{\sqrt p}
=
\sqrt{\frac{L_p}{\ell_p}}
+O_M(L_p^{-M}).
}
\tag{18}
\]

Divide (15) by `sqrt(p)` and insert (18). This proves (4).

The Lambert expansion already recorded in `RE-021` is

\[
\sqrt{\frac{L_p}{\ell_p}}
=
\sqrt2\left(
1-
\frac{\log2}{2L_p}
+O(L_p^{-2})
\right),
\tag{19}
\]

which immediately gives (5). No local-peak condition, no clean adjacent-transition hypothesis, and no bounded-envelope hypothesis has entered.

## 2. Robin failure shifts the reciprocal prime error by the same displacement

For the same state, the exact finite Euler-product factorization used in `RE-021`--`RE-022` is

\[
\log G(C)-\gamma
=
E(p)-T(C)+\log\frac{\log p}{\log X},
\tag{20}
\]

where

\[
E(p)
=
\sum_{r\le p}-\log(1-r^{-1})-\gamma-\log\log p
\]

and

\[
T(C)
:=-\sum_{r\le p}\log(1-r^{-(a_r+1)}).
\]

If `C` violates Robin, then `log G(C)-gamma>0`, so (20) yields the exact strict inequality

\[
\mathcal E_{\pi_\ell}(p)
>
\sqrt p\log p\,T(C)
+
\sqrt p\log p
\log\frac{\log X}{\log p}.
\tag{21}
\]

The universal exponent-tail calculation inherited from `RE-016` and recorded explicitly in `RE-022` gives

\[
\sqrt p\log p\,T(C)
=
\sqrt2+O((\log p)^{-1}).
\tag{22}
\]

For the second term write `X=p+d`. Since (13) gives `d=O(p^0.52)`, Taylor expansion at `p` gives

\[
\sqrt p\log p
\log\frac{\log(p+d)}{\log p}
=
\frac d{\sqrt p}+O(p^{-0.46}).
\tag{23}
\]

Equations (21)--(23) prove (6). Combining (4) with (6) gives (8). This also independently checks the sign and normalization against the mixed coordinate of `RE-009`:

\[
\mathscr Y(p)
=
\mathcal E_{\pi_\ell}(p)
-
\lambda(p)\mathcal E_\vartheta(p),
\qquad
\lambda(p)=1+O(p^{-1}),
\tag{24}
\]

so the two `d/sqrt(p)` terms cancel and the surviving counterexample threshold is again `2sqrt(2)+o(1)`, exactly as required by `RE-021`.

This cancellation is an important audit control. The displacement law does not manufacture a stronger global prime-race theorem; it resolves how the already known mixed threshold is split between its two correlated coordinates at the CA-selected input.

## 3. Local peaks transport the displacement law to ordinary prime gaps

Now suppose `C` is also a regular self-tangent CA local peak. `RE-017` chooses consecutive ordinary primes `u<v` whose first-layer events enclose the complete adjacent CA transition gap:

\[
\eta_{u,1}\le\eta_-<X<\eta_+\le\eta_{v,1}.
\tag{25}
\]

There is no first-layer event between `eta_-` and `eta_+`, and `u,v` are consecutive ordinary primes. Hence `u` is exactly the largest active first-layer prime at `X`, so `p=u`. Since

\[
p\le\eta_{p,1}<X<\eta_{v,1}<v+1,
\tag{26}
\]

one obtains (9):

\[
0<d=X-p<v+1-p=g+1.
\]

If `g=o(sqrt(p))`, then (9) gives `d/sqrt(p)->0`; equations (5)--(6) give (11). This strictly extends the fixed-envelope conclusion of `RE-021`: bounded `g` is not needed for the joint race corner. Every envelope below the square-root scale has the same asymptotic lock.

For the converse branch, failure of `d=o(sqrt(p))` means that some fixed `c>0` and subsequence satisfy `d>=c sqrt(p)`. Equation (9) then forces `g>=c sqrt(p)-1`, proving (12). The currently anchored unconditional prime-gap estimate gives `g=O(p^0.52)`, so any geometric escape from the lock lies in the narrow exponent band between the square-root scale and the best input used by this line.

The implication is deliberately one-way. A square-root-sized envelope does **not** force `d` itself to be square-root-sized: the self-tangent root may sit close to its left first-layer frontier inside a large ordinary prime gap. The intrinsic selector coordinate is `d`, while `g` supplies only the useful upper envelope (9). Treating `g/sqrt(p)` as equal to `d/sqrt(p)` would be an unjustified strengthening.

## 4. Relation to the bounded-envelope event-ladder branch

`RE-018`--`RE-020` show that if `g<=G` is fixed, exceptional boundary transitions can recur only through fixed-base event-ladder near-collisions whose hosts are super-lacunary. `RE-021` then places those hosts at the joint corner

\[
(-\sqrt2,\,\ge\sqrt2)
\]

of the normalized `(theta,pi_l)` race.

The present result separates which part of that conclusion genuinely needs fixed-envelope Diophantine rigidity. The **race lock itself** needs only `d=o(sqrt(p))`, and therefore follows automatically from the much weaker envelope condition `g=o(sqrt(p))`. Fixed `G` is needed only for the finite-base reduction and the Matveev amplification of `RE-020`.

This distinction matters for the growing-envelope chamber left open by the local Mind. There is now a broad intermediate regime

\[
G\to\infty,
\qquad
G=o(\sqrt p),
\tag{27}
\]

in which the fixed-base Diophantine argument no longer applies but the selected joint-race corner remains unchanged. Any future growing-envelope argument can therefore treat the event-ladder combinatorics and the prime-race requirement separately without losing the square-root endpoint calibration.

## 5. Prior-art and novelty boundary

The ingredients are individually established or classical and are already anchored in `SOURCES.md`.

Mantovanelli's August 2026 prime-layer workload preprint is the closest prior art for regular self-tangent CA states, the exact event measure, prime-frontier decomposition, and the unconditional square-root higher-layer correction. In particular, its prime-frontier normal form is consistent with the `-sqrt(2)` Chebyshev scale at self-tangent states; no novelty is claimed for the mere appearance of that constant or for the underlying CA layer thresholds.

Bhattacharya--Martin--Simpson are direct prior art for the normalized standard/reciprocal prime-error coordinates and for the fact that global one-sided control of their mixed difference is RH-equivalent. `RE-009` already turns that result into the strategic restriction that only selector-conditioned correlation can be a weaker route.

Nicolas and Robin provide the classical square-root boundary on the divisor-sum side, while the current Runbo Li short-interval result supplies only the unconditional `p^0.52` envelope used in (13) and after (12).

A fresh targeted search of current Robin/CA work, largest-prime-factor/Chebyshev bounds, Mertens-product formulations, and the recent prime-layer workload literature did not locate the specific selector-conditioned statement (4)--(8): the self-tangent displacement `d=X-p` simultaneously parameterizes the normalized Chebyshev coordinate and the minimum reciprocal-error coordinate of a hypothetical Robin counterexample. The mathematical delta is therefore a repository-level coupling of already anchored structures, not a claim that the constituent prime-error asymptotics or CA threshold formulas are new.

No new source anchor is required.

## 6. Falsification boundaries and research consequence

The self-tangent hypothesis is essential. Equation (15) uses `X=Phi(X)` and is not asserted for arbitrary CA states or arbitrary primes. The all-logarithmic replacement (18) also uses the universal frontier bound `d=O(p^0.52)` from `RE-021`; it is not a pointwise PNT estimate for arbitrary `p`.

Equation (6) is a **necessary condition under Robin failure**, not an unconditional lower bound for `mathcal E_(pi_l)`. Its derivation uses the exact Robin height inequality at the selected state. By `RE-009`, trying to promote the resulting mixed race control to all inputs would again be RH-equivalent.

The result does not rule out square-root or larger consecutive-prime gaps, and it does not show that the joint corner (11) is impossible on CA-selected primes. It also does not extend the fixed-base super-lacunarity of `RE-020` to growing envelopes. Its substantive effect is to narrow the remaining source-conditioned problem into a sharper dichotomy:

\[
\boxed{
\begin{array}{c}
 d=o(\sqrt p)\\[2mm]
 \Downarrow\\[1mm]
 (\mathcal E_\vartheta,\mathcal E_{\pi_\ell})
 \to(-\sqrt2,\,\ge\sqrt2)
\end{array}
}
\qquad\text{or}\qquad
\boxed{
 d\not=o(\sqrt p)
 \Longrightarrow
 g\not=o(\sqrt p).
}
\tag{28}
\]

Thus, across clean and exceptional adjacent-transition chambers alike, a hypothetical self-tangent counterexample peak must either realize a very specific opposite-sign joint prime-race corner or escape through a genuine square-root-scale ordinary-prime envelope. This does not prove Robin's inequality, but it identifies the square-root frontier displacement as the common selector coordinate linking the event geometry to the mixed-race obstruction of `RE-022`.