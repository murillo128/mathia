# WI-039 — the 2026 short-interval Gowers theorem does not directly close the Yang welding layer on its dominant coefficient range

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + PRIOR-ART-REDIRECTION + DECISIVE-NEGATIVE`. The 2026 Matomäki--Radziwiłł--Shao--Tao--Teräväinen short-interval higher-uniformity theorem is materially stronger prior art than the 2019 MRT input audited in WI-034, and at first sight it looks capable of bypassing WI-037's welding-weight gap. A direct plug-in does **not** work: the general affine-linear transference theorem used to turn their Gowers uniformity into prime-pattern asymptotics assumes coefficients bounded by a fixed constant, whereas the exact Yang dispersion swap produces reduced dilation coefficients that grow polynomially with the main scale on all but `o(1)` of the normalized Mertens two-base mass. Even the known higher-dimensional Siegel--Walfisz extension to polylogarithmically growing coefficients therefore covers only an asymptotically negligible part of the Yang continuum ledger.

This is a barrier to a tempting repair route, not a barrier to the one-sided fourth-moment program itself. A coefficient-uniform or anisotropic adaptation that exploits the matched physical scales could still close the welding layer.

## 1. New prior art that has to be checked first

The relevant recent primary source is:

- Kaisa Matomäki, Maksym Radziwiłł, Xuancheng Shao, Terence Tao and Joni Teräväinen, **Higher uniformity of arithmetic functions in short intervals II. Almost all intervals**, *Inventiones mathematicae* 244 (2026), 967--1091, published 26 January 2026; arXiv:2411.05770v2 (23 January 2026), DOI `10.1007/s00222-026-01408-6`.

Their Theorem 1.3(i) proves short-interval Gowers uniformity for `Lambda-Lambda_w` in intervals of length

\[
H\ge X^{1/3+\varepsilon},
\tag{1}
\]

outside an arbitrarily logarithmically sparse exceptional set of interval locations. Theorem 1.5 then deduces an `ell`-point Hardy--Littlewood asymptotic with one averaging variable for almost every `h<=H`; the paper explicitly says that the coefficients `0,1,...,ell-1` may be replaced by **fixed, distinct integers**.

The general transference statement behind that application is Lemma 8.4. For a system of affine-linear forms `Psi=(psi_1,...,psi_t)`, it fixes parameters `s,d,t,L` and assumes that **all linear coefficients of every `psi_i` are bounded by `L`**. The pseudorandom-majorant definition used upstream likewise fixes its coefficient-complexity parameter. Remark 1.4 states that the higher Gowers-norm bounds were intentionally left qualitative because the relevant inverse/contagion dependencies are not quantitatively effective enough to track cleanly.

Thus the published theorem is not uniform for a coefficient bound `L=L(X)` growing like a positive power of `X`.

A second relevant source is Pierre-Yves Bienvenu, **A higher-dimensional Siegel--Walfisz theorem**, *Acta Arithmetica* 179 (2017), 79--100, DOI `10.4064/aa8600-10-2016`. Bienvenu specifically extends the coefficient range in multidimensional prime-pattern asymptotics from fixed coefficients to coefficients growing like a power of `log N`. This is useful context below, but it still stops far short of power-sized coefficients.

Henriot's discriminant-uniform Nair--Tenenbaum estimates supply robust **upper bounds** for arithmetic functions on linear/polynomial forms and are used inside the 2026 paper's pseudorandom-majorant layer. They do not by themselves supply the required prime-pattern asymptotic for power-growing affine coefficients.

## 2. The exact Yang swap exposes the coefficient problem

The pinned Yang source remains

`JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`.

Its `scripts/t2_swaps.py` defines, for fixed `b1,b2`,

\[
A(b_2,j)=\sum_m
\Lambda(m)
\Lambda\!\left(\frac{b_2m+j}{b_1}\right)
1_{b_1\mid b_2m+j},
\tag{2}
\]

with `m` in the locked physical block and `0<|j|<=J`. Expanding `sum_j A(b_2,j)^2` and writing

\[
g=(b_1,b_2),
\qquad
r=\frac{b_1}{g},
\qquad
q=\frac{b_2}{g},
\tag{3}
\]

the equal-lock condition is

\[
b_1(n-n')=b_2(m-m').
\tag{4}
\]

Hence there is an integer `k` with

\[
m'=m-rk,
\qquad
n'=n-qk.
\tag{5}
\]

The four prime factors in the off-diagonal welding term are therefore the affine forms

\[
\boxed{
 m,
\quad m-rk,
\quad n,
\quad n-qk.
}
\tag{6}
\]

The remaining lock/window condition is a convex strip of the form `|b1*n-b2*m|<=J`, plus block endpoints and the removed diagonal. For any fixed `r,q` this is exactly the kind of finite-complexity affine-linear geometry for which Gowers transference is conceptually relevant. But the coefficient norm of (6) is at least

\[
L\ge\max(r,q).
\tag{7}
\]

The question is therefore not whether the 2026 theorem knows about four-point prime patterns in principle; it does. The question is whether its coefficient-uniformity covers the `r,q` actually carrying the Yang mass.

## 3. Polylogarithmic reduced coefficients carry only `o(1)` Mertens mass

WI-033 already proved for the same source normalization that the prime-power measure

\[
\mu_\ell
=\frac1\ell
\sum_{p^a\le X}
\frac{\log p}{p^a}
\delta_{\log(p^a)/\ell},
\qquad
\ell=\log X,
\tag{8}
\]

satisfies uniformly for `0<=u<=1`

\[
\mu_\ell([0,u])
=u+O(1/\ell).
\tag{9}
\]

Fix any `C>0` and put

\[
B_X=(\log X)^C,
\qquad
u_X=\frac{\log B_X}{\ell}
=\frac{C\log\ell}{\ell}.
\tag{10}
\]

Then directly from (9),

\[
\boxed{
\mu_\ell(\{b\le B_X\})
=O\!\left(\frac{\log\ell}{\ell}\right)
=o(1).
}
\tag{11}
\]

The only way large prime powers can nevertheless have a small reduced coefficient in (3) is through a large common factor. For the source's prime-power bases this means the two bases use the same underlying prime (apart from the isolated base-2 family). Its normalized two-base Mertens mass is bounded by

\[
\frac1{\ell^2}
\sum_p
\left(
\sum_{a\ge1}\frac{\log p}{p^a}
\right)^2
=
\frac1{\ell^2}
\sum_p\frac{(\log p)^2}{(p-1)^2}
=O(\ell^{-2}),
\tag{12}
\]

because the prime sum converges. Thus outside `o(1)` of the normalized two-base mass the bases have distinct underlying primes, so `g=1` and

\[
(r,q)=(b_1,b_2).
\tag{13}
\]

Combining (11)--(13), for every fixed `C`,

\[
\boxed{
\text{normalized mass of }
\{\min(r,q)\le(\log X)^C\}
=o(1).
}
\tag{14}
\]

The bounded selector/overlap geometry in WI-033 does not resurrect this set in the continuum limit; WI-033's selector-cancellation estimates were precisely what made the Mertens weak limit legitimate in the actual deterministic normalization.

There is also genuinely power-sized mass. For every fixed `delta>0`, (9) gives

\[
\mu_\ell([0,\delta])=\delta+O(1/\ell),
\tag{15}
\]

so a positive portion of the two-base measure lies where both bases, and generically both reduced coefficients, are at least `X^delta`. Letting `delta` be small makes that portion arbitrarily close to the full unrestricted two-base Mertens mass. The coefficient growth is therefore not a rare tail artifact.

## 4. Why the 2026 theorem cannot simply be inserted

There are three distinct interfaces.

First, **Theorem 1.5 itself is fixed-coefficient**: its stated extension is to any other fixed distinct integer coefficients. Applying it separately for each `(b1,b2)` does not solve this, because the pair changes with `X` and the theorem supplies no error uniform in `L=max(r,q)`.

Second, **Lemma 8.4 is fixed-`L`**. The affine system (6) has exactly the finite-complexity shape that lemma controls after the geometric strip is encoded, but the lemma takes `L` as a fixed parameter before `N->infinity`. Equations (11)--(15) show that one cannot discard the growing-`L` cells as a negligible remainder.

Third, **the known polylogarithmic extension is still too small**. Bienvenu's higher-dimensional Siegel--Walfisz theorem permits coefficient growth by powers of `log N`; equation (14) says that this coefficient regime carries only `o(1)` of the Yang two-base Mertens mass.

Therefore neither the 2026 Gowers theorem nor the 2017 polylog-coefficient extension is, as currently stated, an end-to-end replacement for the welding lemma challenged in WI-037.

## 5. This also kills the naive Abel/maximal shortcut from WI-034

The sliding welding weight has additional structure, so one might instead try summation by parts after WI-034. For fixed `k`, the exact swap writes the weight as a sum of nonnegative twin-prime coefficients over a moving interval in the other variable. Its total variation is bounded by a constant times the total twin-prime mass because each individual interval indicator changes only finitely many times.

Abel summation would then require a **maximal partial-sum bound** for

\[
D_h(x)=
\sum_{n\le x}
\bigl(\Lambda(n)\Lambda(n-h)-\mathfrak S(h)\bigr)
\tag{16}
\]

averaged over the structured shifts. WI-034/MRT 2019 controls the full long-window endpoint in `L^2` over `h`; it does not imply

\[
\sum_h\sup_x|D_h(x)|^2
\ll HX^2(\log X)^{-A}.
\tag{17}
\]

There is no abstract implication from endpoint control to (17): bounded sequences may have zero total sum on every full interval while their prefix maximum is a fixed positive fraction of the interval length (take a positive first half and negative second half). Thus the moving-weight structure does not by itself turn WI-034 into the missing glue estimate.

The 2026 short-interval Gowers theorem is exactly the kind of newer input one should test against this maximality problem, but the power-growing reduced coefficients in (6) prevent a direct use of its published generalized-von-Neumann application. This is why the coefficient issue is load-bearing rather than cosmetic.

## 6. What would actually repair the route

The barrier identifies a narrower target than a new generic four-prime theorem. Any one of the following would suffice in principle:

1. a coefficient-uniform generalized von Neumann / pseudorandom-majorant theorem for the particular system (6), with `r,q` allowed up to the power ranges generated by the Yang covered zone;
2. an **anisotropic** transference theorem whose constants depend on the physical products `rK`, `qK` rather than separately on `r,q`; this is structurally plausible because the Yang locks satisfy matched physical-scale relations of the same kind that made the Gallagher collar automatic in WI-038;
3. a source-specific dispersion argument proving the needed weighted/maximal twin-correlation estimate directly, without passing through a generic affine-linear-forms theorem;
4. a decomposition showing that after denominator contraction the large coefficients can be absorbed into progressions/moduli within an established uniform prime-pattern theorem.

The first route asks for genuinely stronger coefficient uniformity. The second and fourth are more attractive because WI-038 already exhibits an exact cancellation of large dilation factors against shorter prime-sum lengths at the major-arc collar. The present finding does **not** prove that an analogous cancellation exists in the Gowers/minor-arc layer; it makes that the concrete falsifiable target.

## 7. Prior-art and novelty audit

Literature-backed facts are MRSTT 2026 Theorems 1.3 and 1.5, Remark 1.4, their generalized von Neumann Lemma 8.4, Bienvenu's polylogarithmic coefficient extension, Henriot's discriminant-uniform upper bounds, and the classical Mertens estimate underlying WI-033.

Source-backed facts are the exact Yang swap (2)--(6), the prime-power `Lambda(b)/b` weights, and the continuum selector already audited in WI-033.

The exact deductions recorded here are (11)--(15) and their consequence for coefficient coverage: fixed or polylogarithmic reduced dilations occupy only `o(1)` of the relevant normalized two-base Mertens mass, while power-sized coefficients are intrinsic to the continuum ledger. The Abel/maximal counterexample is an elementary information-theoretic no-go showing that full-window `L^2` shift control alone cannot imply the weighted maximal estimate.

Targeted prior-art searches around short-interval Hardy--Littlewood correlations, higher-uniformity/Gowers theorems, coefficient-uniform linear forms in primes, higher-dimensional Siegel--Walfisz, and discriminant-uniform Nair--Tenenbaum bounds did not locate a published theorem that simultaneously supplies the required prime asymptotic and allows the Yang `r,q` to grow like powers of `X`. This absence is **not** a priority claim.

## 8. Decisive audit tests

Reject or narrow this finding if any of the following fails:

1. rederive (5)--(6) directly from `scripts/t2_swaps.py`, including the common-lock equation and the definitions of `r,q`;
2. verify from MRSTT 2026 that Theorem 1.5 permits replacement by **fixed** integer coefficients only and that Lemma 8.4 fixes `L` before the asymptotic;
3. recompute (11) from WI-033 equation (24) with `B_X=(log X)^C`;
4. verify the same-prime-base mass estimate (12), including prime powers rather than primes only;
5. check that the Yang continuum normalization cannot amplify the polylog-base set enough to defeat (14), using WI-033's selector and bounded-geometry estimates;
6. do not treat Bienvenu's polylogarithmic coefficient theorem or Henriot's discriminant-uniform upper bounds as if they provided power-coefficient prime asymptotics;
7. keep the anisotropic/physical-scale repair in Section 6 conjectural until an exact theorem is supplied.

## 9. Consequence for `weil_inertia`

WI-037's welding gap survives the most obvious modern-prior-art substitution. The 2026 short-interval Gowers theorem is highly relevant, but its published transference interface misses precisely the coefficient regime that carries the Yang Mertens continuum. The next efficient question is no longer “is there a newer higher-uniformity theorem?” but

\[
\boxed{
\text{can the matched physical scaling }b_iM_i\asymp X
\text{ be used to remove }r,q
\text{ from the minor-arc/transference constants?}
}
\]

A positive answer would materially advance the one-sided fourth-moment route; absent that, generic fixed/polylog-coefficient Gowers machinery cannot certify the desired welding step.