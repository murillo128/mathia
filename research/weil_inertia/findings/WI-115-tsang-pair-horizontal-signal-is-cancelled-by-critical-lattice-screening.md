# WI-115 — Tsang's pair-level horizontal signal is cancelled at density scale by critical-lattice screening

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY + PRIOR-ART-REDIRECT`. This finding does **not** improve Mathia's unconditional simple-critical zero proportion. It resolves the first low-complexity test in `CLUE-higher-zero-correlations-horizontal-rigidity`: the complex Tsang pair kernel of Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh (BGSTB) is already horizontally sensitive on a same-height mirror pair, so genuine `k>=3` correlations are not needed merely to *detect* horizontal displacement. However, on the exact WI-005/WI-006 critical screening lattice, the complete support-one Tsang pair statistic cancels that same-height excess exactly, and long finite blocks lose only `O(log M)` relative to an on-line-double block. The unconditional Montgomery weight `W(u)=4/(4-u^2)` changes this by only `O(1)` on natural blocks `M=O(L)`. Thus the usable content of the BGSTB horizontal argument is not raw pair-level detectability but the **termwise positivity gate** `|beta-beta'| log T < b`, which permits extraction of the same-height sub-sum before the cross-height cancellation can occur.

The resulting research redirect is sharp: a support-one pair statistic can carry horizontal information locally while still being blind at density scale on the known screening extremizer. To turn the Tsang signal into a new unconditional inertia bound one must control the contribution of pairs outside the positivity strip, obtain a non-screened information carrier, or cross the support-one boundary. Merely adding the complex Tsang kernel to the already available unconditional pair form factor does not by itself defeat WI-005--WI-007.

## 1. Primary-source correction: pair correlation already contains a horizontal discriminator

The current source is S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya and C. L. Turnage-Butterbaugh, **Pair Correlation of Zeros of the Riemann Zeta Function I: Proportions of Simple Zeros and Critical Zeros**, arXiv:2501.14545v3, revised 1 September 2026, https://arxiv.org/abs/2501.14545. The v3 abstract states that, assuming all zeros in `T<gamma<=2T` lie in the box

\[
\left|\beta-\frac12\right|<\frac{b}{2\log T},
\]

with `b=0.3185`, their pair-correlation method proves that at least `2/3` of the zeros are simple and on the critical line. Their Theorem 2 gives the numerical `0.66666908...` bound at `b=0.3185` and recovers the Montgomery--Taylor `0.67250064...` value at `b=0.001`. These are **conditional box results**, not unconditional improvements over Alpöge--Furman.

The structural input relevant here is their complex Tsang kernel. Put

\[
J_b(\alpha):=\frac{j(\alpha)}{\cosh(b\alpha)},
\]

where `j` is either the Fejer kernel `j_F` or the Montgomery--Taylor kernel `j_M`. BGSTB equations (4.3)--(4.4) give

\[
K_b(z)=\frac1{2\pi}\int_{-1}^{1}J_b(\alpha)e^{iz\alpha}\,d\alpha
      =\frac1\pi\int_0^1J_b(\alpha)\cos(z\alpha)\,d\alpha.
\tag{1}
\]

Their Lemma 3 (Tsang) proves

\[
\boxed{\operatorname{Re}K_b(x+iy)>0\qquad(|y|<b),}
\tag{2}
\]

and

\[
K_b(z)\ll_b\frac{e^{|\operatorname{Im}z|}}{1+|z|^2}.
\tag{3}
\]

For a pair of zeros the argument is

\[
-i(\rho-\rho')\log T
=(\gamma-\gamma')\log T-i(\beta-\beta')\log T.
\tag{4}
\]

Thus (2) is a positivity theorem in a microscopic horizontal-difference strip, not a statement that all terms are positive unconditionally.

## 2. A same-height mirror pair has a strict Tsang depth excess

Write

\[
L:=\log T,
\qquad
\delta:=\frac{y}{L},
\]

and compare, at one ordinate `t`, the simple mirror pair

\[
\rho_+=\frac12+\delta+it,
\qquad
\rho_-=\frac12-\delta+it
\tag{5}
\]

with an on-line double zero at `1/2+it`. Counting ordered pairs with multiplicity, the off-line object contributes at equal height

\[
2K_b(0)+K_b(-2iy)+K_b(2iy),
\]

whereas the double contributes `4K_b(0)`. Since `K_b` is even,

\[
\boxed{
D_0(y)
:=2\bigl(K_b(2iy)-K_b(0)\bigr)
=\frac{2}{\pi}\int_0^1J_b(\alpha)
\bigl(\cosh(2y\alpha)-1\bigr)\,d\alpha.
}
\tag{6}
\]

For `j_F` and `j_M`, `J_b>=0` on `[0,1]` and is positive on a set of positive measure, so

\[
\boxed{D_0(y)>0\qquad(y\ne0).}
\tag{7}
\]

This is the lowest-complexity horizontal discriminator asked for by the clue: a double critical zero and a simple off-line mirror pair at the same ordinate are not pair-statistically identical once the complex real-part dependence is retained.

BGSTB already exploit the weaker inequality `cosh u>=1` in their Lemma 5. Retaining the quadratic remainder gives the explicit refinement

\[
\operatorname{Re}K_b\bigl(-i(\beta-\beta')L\bigr)
\ge
A_b+B_b\bigl((\beta-\beta')L\bigr)^2,
\tag{8}
\]

where

\[
A_b:=\frac1\pi\int_0^1J_b(\alpha)\,d\alpha,
\qquad
B_b:=\frac1{2\pi}\int_0^1\alpha^2J_b(\alpha)\,d\alpha>0.
\tag{9}
\]

Therefore, **under the BGSTB positivity/box hypothesis**, their same-height extraction controls not only horizontal multiplicity but also a quadratic horizontal-spread defect. On every horizontal line, functional-equation symmetry makes the multiplicity-weighted mean real part equal to `1/2`, so

\[
\sum_{\substack{\rho,\rho'\\\gamma=\gamma'}}
(\beta-\beta')^2
=
2H(\gamma)
\sum_{\substack{\rho\\\operatorname{Im}\rho=\gamma}}
\left(\beta-\frac12\right)^2.
\tag{10}
\]

This is a genuine conditional defect-to-zero signal. The obstruction below explains why it does not automatically survive after the box assumption is removed.

## 3. Exact support-one cancellation on the WI-005 critical lattice

Place one two-zero object at each critical lattice ordinate

\[
t_j=t_0+j\frac{2\pi}{L},
\qquad j\in\mathbb Z.
\tag{11}
\]

At each `t_j`, compare the off-line pair (5) with an on-line double. For two lattice sites separated by `n=j-k`, equation (4) has real part

\[
x_n=(t_j-t_k)L=2\pi n.
\]

After the two same-sign ordered pairs cancel against two of the four double-zero ordered pairs, the per-site-separation difference is

\[
\begin{aligned}
d_n(y)
&:=K_b(x_n-2iy)+K_b(x_n+2iy)-2K_b(x_n)\\
&=\frac1\pi\int_{-1}^{1}
J_b(\alpha)e^{2\pi in\alpha}
\bigl(\cosh(2y\alpha)-1\bigr)\,d\alpha.
\end{aligned}
\tag{12}
\]

The source kernels satisfy

\[
j_F(\pm1)=j_M(\pm1)=0,
\tag{13}
\]

and the factor `cosh(2y alpha)-1` vanishes at `alpha=0`. Applying Poisson summation to (12), or equivalently summing the absolutely convergent Fourier coefficients using (3), leaves only the integer aliases `alpha=-1,0,1`; all three vanish by (13) and the central zero. Hence

\[
\boxed{
\sum_{n\in\mathbb Z}d_n(y)=0.
}
\tag{14}
\]

In particular, (6) is exactly the `n=0` term, so

\[
\boxed{
\sum_{n\ne0}d_n(y)=-D_0(y)<0.
}
\tag{15}
\]

Thus the same-height off-line excess is not missing from the pair statistic. It is cancelled **exactly** by the change in cross-height pair terms on the critical lattice. This is the pair-correlation analogue of WI-005/WI-006 screening and the support-one alias mechanism in WI-007.

The identity is not special to the detailed Tsang denominator. Any even bandlimited kernel

\[
K(z)=\frac1{2\pi}\int_{-1}^{1}J(\alpha)e^{iz\alpha}\,d\alpha
\]

with `J(+-1)=0` obeys the same cancellation for the symmetric-pair-versus-double replacement. What matters is the support-one endpoint and the critical dual lattice.

## 4. Long finite blocks are asymptotically blind

Let `M` consecutive lattice sites be occupied. The total unweighted Tsang-pair difference between the off-line-pair block and the double-zero block is

\[
\Delta_M(y)
=\sum_{|n|<M}(M-|n|)d_n(y).
\tag{16}
\]

By the decay (3), for fixed `b,y`,

\[
|d_n(y)|\ll_{b,y}\frac1{1+n^2}.
\tag{17}
\]

Using (14),

\[
\Delta_M(y)
=-M\sum_{|n|\ge M}d_n(y)
 -\sum_{|n|<M}|n|d_n(y),
\]

and therefore

\[
\boxed{
|\Delta_M(y)|\ll_{b,y}\log M.
}
\tag{18}
\]

Consequently

\[
\boxed{
\frac{\Delta_M(y)}{M}\longrightarrow0.
}
\tag{19}
\]

This is the density-scale statement relevant to the research program. The local horizontal signal is `Theta(M)` when the `M` same-height pairs are examined in isolation, but the complete support-one pair statistic cancels it to a boundary-size `O(log M)` discrepancy.

## 5. The unconditional Montgomery weight does not rescue natural screening blocks

BGSTB's quantity evaluated unconditionally before the box reduction is not the bare `K_b` sum but

\[
K_b\bigl(-i(\rho-\rho')L\bigr)W(\rho-\rho'),
\qquad
W(u)=\frac4{4-u^2}.
\tag{20}
\]

The weight is important globally, but it does not restore a density-scale horizontal signal on the natural WI screening block. Let

\[
h=\frac{2\pi}{L},
\qquad
a=\frac{2y}{L},
\qquad u_n=nh.
\]

The weighted per-separation difference is

\[
\begin{aligned}
d^{W}_{n,L}(y)
={}&K_b(x_n-2iy)W(a+iu_n)
 +K_b(x_n+2iy)W(-a+iu_n)\\
&-2K_b(x_n)W(iu_n).
\end{aligned}
\tag{21}
\]

Fix `c>0` and restrict to `|n|<=cL`. Since

\[
|W(iu_n)-1|\ll_c\frac{n^2}{L^2},
\tag{22}
\]

and, uniformly on this strip for fixed `y`,

\[
|W(\pm a+iu_n)-W(iu_n)|\ll_{c,y}\frac1L,
\tag{23}
\]

while (3) gives `|K_b(x_n+iv)|<<_{b,y}(1+n^2)^{-1}` for `|v|<=2|y|`, one obtains

\[
\boxed{
|d^W_{n,L}(y)-d_n(y)|
\ll_{b,c,y}
\left(\frac1{L^2}+\frac1{L(1+n^2)}\right).
}
\tag{24}
\]

Therefore for every natural block `M<=cL`,

\[
\sum_{|n|<M}(M-|n|)
\bigl(d^W_{n,L}(y)-d_n(y)\bigr)=O_{b,c,y}(1),
\tag{25}
\]

and (18) yields

\[
\boxed{
\Delta^W_M(y)=O_{b,c,y}(\log M)=o(M).
}
\tag{26}
\]

So the exact `W`-weighted form-factor observable that precedes BGSTB's box reduction is also asymptotically blind on the finite critical-lattice screening block. This does **not** claim that every global zeta-like arrangement is invisible to `W`; it closes the direct hope that the existing unconditional pair form factor itself supplies a density-scale discriminator against the already known WI-005/WI-006 extremizer.

## 6. Why the BGSTB box argument escapes the cancellation

There is no contradiction between (14) and BGSTB's horizontal theorem. Their Lemma 3 proves termwise positivity only when

\[
|\beta-\beta'|L<b.
\tag{27}
\]

Their box assumption places every zero within `b/(2L)` of the critical line, so **every ordered pair** satisfies (27). This lets Lemma 5 discard all cross-height terms and keep only

\[
\gamma=\gamma',
\]

where (6)--(8) carry the horizontal signal. The screening cancellation (15) works by changing the cross-height contribution relative to the double-zero configuration; positivity of the individual terms does not prevent that difference from being negative.

Without a theorem that makes the complement of (27) harmless, the unconditional evaluation of the full pair sum cannot justify the same-height extraction. BGSTB explicitly state this dependence: Theorem 2 assumes the narrow box, and their Remark 3 says it can instead be replaced by a **suitably strong Zero Density Hypothesis**. They do not provide an unconditional theorem eliminating that gate.

Thus the actual information flow is

\[
\boxed{
\text{complex pair kernel}
+\text{ microscopic termwise positivity}
\Longrightarrow
\text{same-height extraction}
\Longrightarrow
\text{horizontal multiplicity/depth control},
}
\tag{28}
\]

not

\[
\text{unconditional support-one pair form factor}
\Longrightarrow
\text{horizontal depth control}.
\]

## 7. Relation to WI-005--WI-007 and research consequence

WI-005 shows that the negative inertia of isolated off-line Weil blocks can be screened by a critical vertical lattice. WI-006 strengthens this to operator equivalence between screened off-line pairs and on-line doubles. WI-007 proves that every Alpöge--Furman-type auxiliary compression with support at most one is exactly blind to that replacement, with horizontal depth returning only through nonzero Poisson aliases after support one is crossed.

The present calculation is not a restatement of those compressed-operator results. It audits a different information carrier from the recent pair-correlation literature and finds the same support-one obstruction in scalar pair-statistic form:

\[
\boxed{
\begin{array}{c}
\text{same-height Tsang pair term sees horizontal depth exactly},\\
\text{full critical-lattice support-one pair sum cancels it exactly},\\
\text{finite natural blocks retain only }O(\log M)=o(M)\text{ discrepancy},\\
\text{the unconditional Montgomery weight changes this by only }O(1).
\end{array}}
\tag{29}
\]

This materially narrows `CLUE-higher-zero-correlations-horizontal-rigidity`. The first escalation should **not** be to genuine higher correlations merely to obtain a horizontal-sensitive formula: BGSTB already provide one at pair level. The missing unconditional bridge is instead a mechanism that prevents or quantitatively charges the compensating cross-height terms. Plausible interfaces are: a proved control of the pairs outside the Tsang positivity strip; a pair statistic with arithmetic access whose depth signal survives the WI screening lattice; or supercritical Fourier support, where WI-007 says the first nonzero alias can carry depth but new prime-pair arithmetic becomes load-bearing. Genuine `k`-point information remains a separate possible escape only if it evades this support-one screening quotient.

## 8. Prior-art and novelty audit

The primary literature contribution used here is BGSTB arXiv:2501.14545v3: equations (4.3)--(4.6) give the complex Tsang kernel and its unconditional pair-sum evaluation, Lemma 3 gives positivity in `|Im z|<b`, Lemmas 4--5 use the narrow-box hypothesis to remove `W`, keep a positive pair sum, and bound horizontal multiplicity, and Theorems 1--2 convert that into conditional simple-critical proportions. The revised v3 source was checked directly rather than relying on an informal summary.

Mathia's prior WI-005--WI-007 already establish the critical-lattice screening/alias mechanism for compressed Weil operators. The exact identities (12)--(19) and the `W`-stability estimate (24)--(26) are the derived bridge between that persisted screening extremizer and the BGSTB Tsang pair statistic. No claim of external priority is made for this bridge; it is stored because it decisively changes which part of the higher-correlation clue is worth pursuing.

The finding is deliberately negative about only one route. It does **not** show that all pair statistics are blind, that higher correlations are unnecessary for stronger results, or that a suitably strong unconditional zero-density/cross-pair estimate cannot make the BGSTB mechanism effective. It shows that the already available support-one Tsang/Montgomery pair observable, taken as a complete density-scale statistic without the box positivity extraction, does not distinguish the canonical WI screening configuration from on-line doubles at leading order.
