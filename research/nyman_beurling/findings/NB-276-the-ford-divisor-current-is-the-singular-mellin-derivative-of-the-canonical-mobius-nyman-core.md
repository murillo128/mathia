# NB-276 — The Ford divisor current is the singular Mellin derivative of the canonical Möbius Nyman core

**Date:** 2026-09-22  
**Status:** `EXACT-DERIVED + SOURCE-TO-FORD-BRIDGE + CANONICAL-NYMAN-SYNTHESIS + MOBIUS-DERIVATIVE + EULER-POLE-CANCELLATION + MEROMORPHIC-CONTINUATION + UNBOUNDED-HARDY-BRIDGE + NB-020/NB-237/NB-275-COUPLING + METHOD-REDUCTION + PRIOR-ART-AUDITED`.

`NB-275` shows that the resolved Ford channel itself is almost orthogonal to the canonical Nyman target after carrier demodulation. It therefore leaves a very specific question: **what operation actually connects the Ford logarithmic-derivative current to the canonical Nyman source geometry?** Treating both objects as if they lived in one bounded Hilbert channel is no longer viable.

There is an exact source-level answer. Write the canonical Hardy synthesis of a Dirichlet source `P` as

\[
\mathcal N[P](s)
:=
\frac{\zeta(s)}s\bigl(P(s)-P(1)\bigr).
\tag{1}
\]

For the basis source `P_k(s)=k^{-s}`, this is exactly the canonical generator

\[
\mathcal N[P_k](s)
=
\left(k^{-s}-k^{-1}\right)\frac{\zeta(s)}s
=G_k(s).
\tag{2}
\]

The formal exact source of the Nyman target is the reciprocal-zeta core

\[
P_*(s)=\frac1{\zeta(s)},
\qquad
P_*(1)=0,
\tag{3}
\]

because

\[
\mathcal N[P_*](s)=\frac1s=E(s).
\tag{4}
\]

Now differentiate the **source before synthesis**. Since

\[
P_*'(s)=-\frac{\zeta'(s)}{\zeta(s)^2},
\qquad
P_*'(1)=1,
\tag{5}
\]

one obtains the exact meromorphic identity

\[
\boxed{
\mathcal N[P_*'](s)
=-\frac1s
\left(
\frac{\zeta'}{\zeta}(s)+\zeta(s)
\right).
}
\tag{6}
\]

Equivalently,

\[
\boxed{
\frac{\zeta'}{\zeta}(s)
=
-s\,\mathcal N[P_*'](s)-\zeta(s).
}
\tag{7}
\]

The correction `+zeta` is not an arbitrary regularizer. It is exactly the term created by the canonical Euler anchor `P(s)-P(1)`, because `P_*'(1)=1`. At `s=1`, the pole of `zeta'/zeta` has residue `-1` while the pole of `zeta` has residue `+1`; hence

\[
\frac{\zeta'}{\zeta}(s)+\zeta(s)
\tag{8}
\]

is regular at the Euler pole. At every zero `rho` of multiplicity `m(rho)`, however, `zeta` vanishes and `zeta'/zeta` has residue `m(rho)`. Therefore the meromorphic current

\[
-s\,\mathcal N[P_*'](s)
=
\frac{\zeta'}{\zeta}(s)+\zeta(s)
\tag{9}
\]

has **the same zero poles with the same residues as the Ford logarithmic derivative, but no pole at `1`**.

Thus the Ford divisor current is not unrelated to the canonical Nyman source. It is the meromorphic, `s`-weighted image of the Mellin derivative of the same reciprocal-zeta source whose undifferentiated synthesis is the target. This bridge is exact, but it is singular: it does not define a bounded operator on the Nyman Hardy space. That distinction reconciles the strong Ford residue effects with the target invisibility found in `NB-275`.

## 1. Canonical synthesis turns the reciprocal-zeta source into the target

The canonical generators from `NB-001` are

\[
G_k(s)
=
\left(k^{-s}-k^{-1}\right)\frac{\zeta(s)}s,
\qquad k\ge2.
\tag{10}
\]

For a finite Dirichlet polynomial

\[
P(s)=\sum_k a_k k^{-s},
\tag{11}
\]

the corresponding finite Nyman combination is

\[
\sum_k a_kG_k(s)
=
\frac{\zeta(s)}s
\left(
\sum_k a_kk^{-s}-\sum_k\frac{a_k}{k}
\right)
=
\mathcal N[P](s).
\tag{12}
\]

So `(1)` is not a new model; it is simply the canonical discrete synthesis written on its source Dirichlet polynomial.

In the absolutely convergent half-plane,

\[
\frac1{\zeta(s)}
=
\sum_{k\ge1}\frac{\mu(k)}{k^s}.
\tag{13}
\]

Moreover, `1/zeta` has a simple zero at `s=1`, so its analytic continuation satisfies

\[
P_*(1)=0.
\tag{14}
\]

Substituting `(3)` into `(1)` gives `(4)` immediately:

\[
\mathcal N[P_*](s)
=
\frac{\zeta(s)}s\frac1{\zeta(s)}
=
\frac1s.
\tag{15}
\]

This is the source-side version of the familiar Möbius heuristic behind Nyman--Báez-Duarte approximation. It also explains why the low-index coefficient core in `NB-020` locks to a Möbius pattern, up to that finding's real-space sign convention: the exact reciprocal source of the target is `1/zeta`.

The point needed here is not merely that Möbius coefficients occur. It is that **the Ford current appears after differentiating this same exact source**.

## 2. Differentiating the target source produces the logarithmic derivative

Differentiate `(3)`:

\[
P_*'(s)
=
-\frac{\zeta'(s)}{\zeta(s)^2}.
\tag{16}
\]

Near `s=1`, write `z=s-1`. Since

\[
\zeta(s)=\frac1z+O(1),
\qquad
\frac1{\zeta(s)}=z+O(z^2),
\tag{17}
\]

we have

\[
P_*'(1)=1.
\tag{18}
\]

Applying the **same** canonical synthesis `(1)` to the differentiated source gives

\[
\begin{aligned}
\mathcal N[P_*'](s)
&=
\frac{\zeta(s)}s
\left(
-\frac{\zeta'(s)}{\zeta(s)^2}-1
\right)\\
&=
-\frac1s
\left(
\frac{\zeta'}{\zeta}(s)+\zeta(s)
\right),
\end{aligned}
\tag{19}
\]

which proves `(6)`.

The cancellation at the Euler pole is exact. Using the Laurent expansions

\[
\frac{\zeta'}{\zeta}(s)
=-\frac1{s-1}+O(1),
\qquad
\zeta(s)
=\frac1{s-1}+O(1),
\tag{20}
\]

the sum in `(8)` is holomorphic at `1`. At a nontrivial or trivial zero `rho`, on the other hand,

\[
\frac{\zeta'}{\zeta}(s)
=
\frac{m(\rho)}{s-\rho}+O(1),
\qquad
\zeta(s)=O\!\left((s-\rho)^{m(\rho)}\right),
\tag{21}
\]

so

\[
\operatorname*{Res}_{s=\rho}
\left[-s\mathcal N[P_*'](s)\right]
=m(\rho).
\tag{22}
\]

The canonical anchor has therefore performed exactly the regularization that the Ford divisor problem wants: it removes the pole of `zeta` itself while leaving every zero residue untouched.

This also clarifies why replacing `zeta'/zeta` by the pole-cancelled current is harmless in the first-order Ford representation. For any compactly supported smooth test `Psi` whose support lies in a region where the only meromorphic singularities under discussion are zeta zeros,

\[
\int_{\mathbb C}
\zeta(s)\,\bar\partial\Psi(s)\,dA(s)=0,
\tag{23}
\]

by distributional integration by parts because `zeta` is holomorphic there. Consequently

\[
\boxed{
\int
\frac{\zeta'}{\zeta}(s)\bar\partial\Psi(s)\,dA(s)
=
-\int
s\mathcal N[P_*'](s)\bar\partial\Psi(s)\,dA(s).
}
\tag{24}
\]

For the compactly depth-localized Ford tests of `NB-237`/`NB-249`, the pole at `1` is outside the critical layer for large `J`; alternatively `(20)` shows that the pole-cancelled current itself is regular there. Thus `(24)` identifies the exact current seen by the Ford zero residue with the differentiated canonical source.

No Hilbert-space estimate has been used in `(24)`. It is an identity of meromorphic/distributional currents.

## 3. The bridge is the logarithmic derivative of the Möbius coefficient core

Equation `(16)` has the Dirichlet-series form

\[
P_*'(s)
=-
\sum_{k\ge2}
\frac{\mu(k)\log k}{k^s},
\qquad \Re s>1.
\tag{25}
\]

Hence the differentiated source is precisely the Möbius core with one Mellin-frequency factor `log k` inserted. This is the coefficient-level relation between the early finite-section geometry and the later Ford source geometry:

\[
\mu(k)
\quad\longmapsto\quad
-\mu(k)\log k.
\tag{26}
\]

That factor is exactly what Mellin differentiation does to the atom `k^{-s}`.

To make the ancestry from **finite legal Nyman vectors** explicit, fix `epsilon>0` and truncate at `M`:

\[
P_{\epsilon,M}(s)
:=
\sum_{k\le M}
\mu(k)k^{-\epsilon}k^{-s}.
\tag{27}
\]

Then

\[
P_{\epsilon,M}'(s)
=-
\sum_{k\le M}
\mu(k)\log k\,k^{-\epsilon}k^{-s},
\tag{28}
\]

and

\[
\mathcal N[P_{\epsilon,M}'](s)
=
-
\sum_{2\le k\le M}
\mu(k)\log k\,k^{-\epsilon}G_k(s)
	ag{29}
\]

is an ordinary finite canonical Nyman combination.

For fixed `epsilon>0`, the limit `M->infinity` is absolutely convergent on every compact subset of `Re s>1`, and

\[
P_\epsilon(s)
:=
\lim_{M\to\infty}P_{\epsilon,M}(s)
=
\frac1{\zeta(s+\epsilon)}.
\tag{30}
\]

Therefore

\[
P_\epsilon'(s)
=-\frac{\zeta'(s+\epsilon)}{\zeta(s+\epsilon)^2}.
\tag{31}
\]

As `epsilon downarrow0`, locally uniformly on `Re s>1`,

\[
P_\epsilon\to P_*=rac1\zeta,
\qquad
P_\epsilon'\to P_*'.
\tag{32}
\]

Thus the meromorphic bridge `(6)` has a precise two-stage source ancestry:

1. finite legal Nyman combinations with coefficients `-mu(k) log k k^{-epsilon}`;
2. first `M->infinity`, then `epsilon->0` on the Euler half-plane;
3. meromorphic continuation of the resulting closed form to the Ford region.

The order matters. Nothing here says that the finite vectors converge in the Nyman `H^2` norm as `epsilon->0`, nor that one may continue the coefficient series term by term through the critical strip. The only claimed continuation is that of the **closed meromorphic function** obtained on `Re s>1`.

That limitation is the essential mathematical content rather than a technical nuisance.

## 4. Why this does not contradict the target invisibility of `NB-275`

`NB-275` proves that the direct resolved Ford shell span, after the legal Hardy projection and carrier demodulation, sees only exponentially small canonical target mass. Equation `(6)` does not put the Ford current back into that bounded span. It shows that the current is reached by two operations that are singular from the Nyman-Hardy viewpoint.

The first is source differentiation. On a logarithmic shell `log k\asymp X`, differentiation multiplies the source atom by

\[
\log k\asymp X.
\tag{33}
\]

So even before any continuation, the bridge is not neutral in the source metric. This is the same Mellin-frequency tariff that repeatedly appears in `NB-213`--`NB-218`, now attached to the **canonical target source** rather than to an auxiliary primitive.

The second is the multiplier by `s` in `(7)`. On the Nyman Hardy space this multiplier is unbounded. The canonical target itself gives the elementary witness:

\[
E(s)=\frac1s\in H^2(\Re s>1/2),
\qquad
sE(s)=1\notin H^2(\Re s>1/2).
\tag{34}
\]

Therefore no bounded-Hardy argument may transport a norm estimate from `mathcal N[P_*']` to the Ford current simply by multiplying by `s`.

There is a third singularity hidden in the limiting procedure: the reciprocal-zeta source and its derivative acquire the zero divisor under meromorphic continuation. The finite vectors `(29)` are entire members of the canonical finite span, while the limiting current `(6)` has poles at zeta zeros. Hence the Ford residue is created only after a limit/continuation operation that is not norm-continuous in the canonical Hardy geometry.

This explains the apparent tension between the recent findings:

- `NB-269`--`NB-275` show that bounded resolved Ford channels can have vanishing Hardy energy and essentially zero target access;
- `(6)` shows that the actual divisor current is obtained from the canonical target source only after differentiation, singular continuation and multiplication by `s`.

So the missing Ford-to-Nyman bridge is **not another bounded positive Gram correction inside the channel classified by `NB-271`**. The natural exact bridge already has the kind of unbounded/global strength that `NB-271` said a successful repair would need.

This does not prove that the singular bridge yields a useful Nyman lower bound. It identifies where such a bound would have to pay its analytic cost.

## 5. A sharper next target: finite regularization cost at Ford scale

The current frontier can now be stated without an unspecified "nonlocal operator". Take the finite legal differentiated-Möbius vectors `(29)` and ask how large `M=M(X)` and how small `epsilon=epsilon(X)` must be before their source-side current reproduces the Ford logarithmic derivative at carrier scale `X` with an error small enough to survive the contour shift.

A crude absolute-value audit already shows why this is nontrivial. On

\[
\sigma_X=1+\frac rX,
\tag{35}
\]

the unsigned tail of the differentiated Dirichlet series obeys

\[
\sum_{k>M}
\frac{\log k}{k^{1+r/X}}
\ll
M^{-r/X}
\left(
\frac{X\log M}{r}
+\frac{X^2}{r^2}
\right).
\tag{36}
\]

Thus an argument that throws away Möbius cancellation needs `r log M/X` to beat at least the logarithm of the polynomial prefactor. Merely taking `log M\asymp X` does not make `(36)` small. This is only an **absolute-method boundary**, not a lower bound on the true Möbius truncation error; cancellation may do much better.

The useful next problem is therefore precise:

> Quantify the Ford-scale approximation of the meromorphic current `(6)` by the finite legal Nyman vectors `(29)`, while tracking the actual `H^2` cost and keeping Möbius cancellation coupled to the contour test.

If this can be done with controlled Hardy cost, it supplies the first genuine source-to-destination bridge missing from `NB-275`. If the required norm or coefficient budget diverges faster than the Nyman target gain, the Ford route becomes a dual diagnostic only and cannot close the approximation problem.

This is a materially narrower question than searching for another abstract off-diagonal Gram.

## 6. Adversarial audit

### 6.1 The identity is source-level and meromorphic, not an `H^2` convergence theorem

The strongest possible overclaim would be to read `(6)` as saying that

\[
\mathcal N[P_*']
\]

is itself a legal canonical Nyman vector. That has **not** been shown. The rigorous finite-span ancestry is `(27)`--`(32)` on `Re s>1`; the passage into the critical strip is by meromorphic continuation of the closed form. Any use in a Nyman norm estimate must separately justify the limiting operation.

### 6.2 The `+zeta` term cannot simply be dropped pointwise

Equation `(7)` contains an additive `-zeta` correction. It is invisible only in a divisor/`bar partial` pairing such as `(24)`, where holomorphic terms are annihilated, or in an equivalent closed-contour argument. It is not pointwise small on the Ford line and should not be discarded by magnitude.

### 6.3 Multiplication by `s` is a real cost

The factor `s` in `(7)` is not harmless normalization. Equation `(34)` proves directly that it is unbounded on the Hardy space containing the Nyman target. Any future coercive transfer must work in a graph norm/domain that controls this multiplier or keep the `1/s` target weight explicitly.

### 6.4 No claim is made that every successful bridge must equal `(6)`

The finding identifies a natural exact bridge generated by the canonical reciprocal-zeta source. It does not exclude a different bounded representation that uses additional arithmetic structure. What it does rule out is treating the most direct logarithmic-derivative bridge as if it were a bounded perturbation of the resolved Ford `H^2` channel.

### 6.5 The finite truncation estimate `(36)` is only a black-box audit

The Möbius signs are discarded in `(36)`. It is therefore not a necessity theorem and must not be used to infer that `M` is intrinsically exponential at a particular rate. The next useful work is precisely to retain the signed correlation.

## 7. Prior-art boundary

The ingredients behind `(1)`--`(6)` are classical individually. The Hardy/Mellin Nyman synthesis and canonical generators are anchored through Bagchi and Báez-Duarte in `SOURCES.md`; the reciprocal-zeta Dirichlet series with Möbius coefficients and its differentiation are standard Euler-product identities. Báez-Duarte's work explicitly places Möbius sums at the heart of strong Nyman--Beurling criteria. A fresh search also returned the classical Báez-Duarte papers on arithmetic Nyman criteria and Möbius convolutions, but did not locate this specific coupling of the differentiated reciprocal-zeta source to the first-order Ford divisor current.

No theorem-level novelty is claimed for differentiating `1/zeta` or for the identity `sum mu(k)k^{-s}=1/zeta(s)`. The line-local contribution is the exact factorization

\[
\boxed{
E=\mathcal N[1/\zeta],
\qquad
\frac{\zeta'}{\zeta}
=-s\,\mathcal N[(1/\zeta)']-\zeta,
}
\tag{37}
\]

together with the observation that the canonical anchor correction cancels the Euler pole while preserving every zero residue, and the consequent method boundary that the Ford-to-Nyman passage is singular/unbounded in the native Hardy norm.

No new external theorem is load-bearing beyond sources already anchored in `SOURCES.md`, so this finding does not require a source-file update.

## 8. Conclusion

`NB-275` showed that the direct resolved Ford band is the wrong target-bearing Hilbert channel. The present identity identifies what was missing: **the Ford logarithmic derivative is obtained by differentiating the canonical reciprocal-zeta source, applying the same Nyman synthesis, and then removing the target's `1/s` weight through the unbounded multiplier `s`.**

The `-k^{-1}` Euler anchor is not incidental. After source differentiation it produces the `+zeta` correction that cancels the pole at `1`, leaving a meromorphic current whose poles are exactly the zeta zeros with their correct multiplicities. In that precise sense the Ford divisor current is already encoded in the canonical Nyman source geometry.

But it is encoded through a singular operation, not through the bounded resolved channel ruled out by `NB-269`--`NB-275`. The next discriminating calculation is now finite and quantitative: approximate `(37)` by the legal truncated vectors `(29)` at Ford scale and measure the required Hardy cost. That is the first place where the source-side Ford mechanism can genuinely succeed or fail as a Nyman approximation bridge.