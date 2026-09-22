# MC-466 — Original-shift Fejér envelope cancels the apparent outer-gcd advantage

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-465` proves that, for a fixed outer pair, favorable normalized-gcd classes remain sparse under the standard Fejér/van-der-Corput shift weights. Its compatible-shift ratio is

\[
\frac{F_Q}{D_Q(g)}
\ll \frac{M^2}{r_2},
\qquad
r'=g r_2,
\qquad
g=(r,r').
\tag{1}
\]

Because `r_2=r'/g`, this ratio superficially leaves a possible escape: outer sieve coefficients might concentrate on pairs with large common factor `g`, making the normalized quotient small and the compatible favorable fraction large.

For the **standard original-shift Fejér envelope**, that apparent gain cancels exactly against the loss of compatible shifts.

Let

\[
g=(r,r'),
\qquad
r=g r_1,
\qquad
r'=g r_2,
\qquad
h=g h_0
\tag{2}
\]

for a compatible nonzero shift `h`. The normalized quotient from `MC-463`--`MC-465` satisfies the exact identity

\[
\boxed{
T(h_0)
=
\frac{r_2}{(h_0,r_2)}
=
\frac{r'}{(h,r')}.
}
\tag{3}
\]

Thus the source-support admission condition is a statement about the part of the **original outer divisor `r'` not absorbed by the original shift `h`**. The first outer divisor `r` enters only through the compatibility requirement `g\mid h`.

For Fejér bandwidth `Q>=1`, define the positive-shift favorable mass for this pair by

\[
F_Q(r,r';M)
:=
\sum_{\substack{1\le h<Q\\g\mid h\\r'/(h,r')\le M}}
(Q-h).
\tag{4}
\]

Then there is an exact original-variable decomposition

\[
\boxed{
F_Q(r,r';M)
=
\sum_{\substack{T\mid r'/g\\T\le M}}
\ \sum_{\substack{1\le a\le \lfloor (Q-1)T/r'\rfloor\\(a,T)=1}}
\left(Q-\frac{r'}{T}a\right).
}
\tag{5}
\]

In particular, with the unrestricted positive-shift Fejér mass

\[
E_Q:=\sum_{h=1}^{Q-1}(Q-h)=\frac{Q(Q-1)}2,
\tag{6}
\]

one has for every pair `(r,r')`, every `M>=1`, and every `Q>=1`,

\[
\boxed{
F_Q(r,r';M)
\le
E_Q\,
\min\!\left(1,\frac{M(M+1)}{r'}\right).
}
\tag{7}
\]

The bound is independent of `g=(r,r')`.

Consequently, let `c_{r,r'}>=0` be **any** outer coefficient-pair mass independent of the van-der-Corput shift. Allow the support threshold to vary with the pair, writing `M_{r,r'}`. Then

\[
\boxed{
\sum_{r,r'}c_{r,r'}F_Q(r,r';M_{r,r'})
\le
E_Q
\sum_{r,r'}c_{r,r'}
\min\!\left(1,
\frac{M_{r,r'}(M_{r,r'}+1)}{r'}
\right).
}
\tag{8}
\]

In a cell on which

\[
r'\ge R,
\qquad
M_{r,r'}\le M_*,
\tag{9}
\]

this gives the coefficient-independent envelope

\[
\boxed{
\frac{
\sum c_{r,r'}F_Q(r,r';M_{r,r'})
}{
E_Q\sum c_{r,r'}
}
\le
\min\!\left(1,
\frac{M_*(M_*+1)}{R}
\right).
}
\tag{10}
\]

Equation `(10)` applies directly to absolute outer-product mass `c_{r,r'}=|\alpha_r\alpha_{r'}|`, quadratic mass `c_{r,r'}=|\alpha_r|^2|\alpha_{r'}|^2`, or any other nonnegative envelope carried by the same shift-independent outer coefficients. Therefore **concentration of the outer coefficients on large-`g` pairs is not by itself a way around the `MC-464`--`MC-465` sparsity barrier** for the standard Fejér architecture. Large `g` makes a larger fraction of the *compatible* shifts favorable, but it reduces the number of compatible original shifts by the same scale.

What remains open is narrower. A large gcd can still change the pair-dependent interval length and hence the threshold `M_{r,r'}` itself; the outer coefficients can concentrate on small `r'`; the aggregated residual coefficients can have nontrivial participation; and the aligned unexpanded amplitude can correlate with the surviving shifts. Equation `(10)` controls only the favorable **outer shift/coefficient mass**, not the full oscillatory amplitude.

No conductor-power saving, bound for `M(x)`, or RH consequence follows.

## 1. The normalized quotient is already an original-variable quotient

Since `g\mid h` and `g\mid r'`,

\[
(h,r')
=(g h_0,g r_2)
=g(h_0,r_2).
\tag{11}
\]

Therefore

\[
\frac{r'}{(h,r')}
=
\frac{g r_2}{g(h_0,r_2)}
=
\frac{r_2}{(h_0,r_2)},
\tag{12}
\]

which proves `(3)`.

This identity removes an ambiguity in the fixed-pair normalization. The favorable support condition is not intrinsically a condition on the pair gcd `g`; it is a condition on how much of `r'` survives after taking its gcd with the **original** shift.

For one-sided staging the role of `r'` is asymmetric because the first residual block was expanded and the second retained. Reversing the staging gives the analogous quotient `r/(h,r)` on the other side. No symmetry stronger than that is asserted here.

## 2. Exact original-shift parameterization

Fix a favorable compatible shift and put

\[
T=\frac{r'}{(h,r')}.
\tag{13}
\]

Compatibility gives `g\mid(h,r')`, so `T\mid r'/g`. Put

\[
d=(h,r')=\frac{r'}{T}.
\tag{14}
\]

Then every integer with this exact gcd has the unique form

\[
h=da=\frac{r'}{T}a,
\qquad
(a,T)=1.
\tag{15}
\]

Conversely, if `T\mid r'/g` and `(a,T)=1`, then `d=r'/T` is divisible by `g`, so the resulting shift is compatible and satisfies `(h,r')=d`. The Fejér range `1\le h<Q` is exactly

\[
a\le \frac{(Q-1)T}{r'}.
\tag{16}
\]

Substituting `(15)` into the weight `Q-h` proves `(5)`.

Equation `(5)` is the original-variable form of `MC-465` equation (11). Its useful feature is that all explicit `g`-dependence has moved into the harmless divisor restriction `T\mid r'/g`; the shift location and weight are determined by `r'` and `T` themselves.

## 3. The absolute Fejér envelope has no gcd gain

Drop both the coprimality condition and the divisor restriction in `(5)`. For each `T<=M`, the number of possible `a` is at most

\[
\frac{(Q-1)T}{r'},
\tag{17}
\]

and each Fejér weight is at most `Q`. Hence

\[
\begin{aligned}
F_Q(r,r';M)
&\le
\frac{Q(Q-1)}{r'}
\sum_{T\le M}T\\
&=
\frac{Q(Q-1)}2
\frac{M(M+1)}{r'}\\
&=E_Q\frac{M(M+1)}{r'}.
\end{aligned}
\tag{18}
\]

The trivial bound `F_Q<=E_Q` gives `(7)`.

The same conclusion follows directly from `MC-465` before its compatible-mass normalization. There,

\[
F_Q
\le
\frac{QX M(M+1)}{2r_2},
\qquad
X=\left\lfloor\frac{Q-1}{g}\right\rfloor.
\tag{19}
\]

Using

\[
X\le\frac{Q-1}{g},
\qquad
r_2=\frac{r'}g,
\tag{20}
\]

cancels `g` and reproduces `(18)`. Thus `(18)` is not a new estimate hidden behind an approximation; it is the exact compensation already latent in the pre-normalized `MC-465` count.

If positive and negative nonzero shifts are both used with the symmetric Fejér kernel, both the favorable mass and `E_Q` double, so the ratio in `(7)`--`(10)` is unchanged.

## 4. Arbitrary outer coefficient concentration cannot restore the missing gcd factor

Multiply `(7)` by any nonnegative coefficient-pair mass `c_{r,r'}` and sum. This proves `(8)` immediately. No regularity, sign pattern, factorability, or equidistribution hypothesis on the coefficients is required; only independence from the later shift variable is used.

For a signed well-factorable component, take

\[
c_{r,r'}=|\alpha_r\alpha_{r'}|
\tag{21}
\]

when measuring absolute coefficient mass. For a positive quadratic closure, take

\[
c_{r,r'}=|\alpha_r|^2|\alpha_{r'}|^2.
\tag{22}
\]

Both obey `(8)` exactly. On a cell satisfying `(9)`, pull the uniform factor out of the sum to obtain `(10)`.

This identifies the compensation hidden by the compatible-shift ratio in `MC-465`:

\[
\text{favorable fraction among compatible shifts}
\sim \frac{gM^2}{r'},
\qquad
\text{compatible-shift supply}
\sim \frac1g,
\tag{23}
\]

so their product is on the `M^2/r'` scale.

The statement is deliberately about the **original positive Fejér envelope** rather than the ratio to `D_Q(g)`. A proof that concentrates outer coefficients on large-gcd pairs may indeed make almost every *surviving compatible shift* favorable, but it simultaneously leaves fewer original shifts for those pairs. For an upper-bound argument this is a cost, not a free source of information.

## 5. What can still evade the envelope

Equation `(10)` does not close the staged branch.

First, the exact support threshold is

\[
M_{r,r'}
=
\left\lceil\frac{S L_{r,r'}}{p-L_{r,r'}}\right\rceil-1,
\tag{24}
\]

when the common-length reduction used in `MC-464` is valid. The interval length `L_{r,r'}` depends on the outer arithmetic geometry. A large pair gcd can therefore help **indirectly** if it makes `L_{r,r'}` large enough to increase `M_{r,r'}`. The present cancellation removes only the direct `r_2=r'/g` gain in the shift-mass ratio.

Second, coefficients can concentrate on small `r'`, where the denominator in `(7)` is weak. Any useful global argument must therefore retain the real support ranges of the well-factorable component rather than replacing them by an artificial uniform lower scale.

Third, `(8)` does not include the aggregated residual coefficient `\widetilde\beta(s_0)` or the aligned amplitude

\[
B_\beta(C_{s_0}+r_1s_0j).
\tag{25}
\]

Those objects can correlate with the favorable outer cells. They must be estimated jointly before positive closure; replacing them by unrelated sup norms would return to an already-classified lossy bound.

Finally, a shift-dependent or non-Fejér arithmetic weighting lies outside `(8)`. In the standard q-vdC setup the sieve coefficients are fixed before the differencing shift is chosen. A method that deliberately makes the coefficient/filter architecture depend on `h` is a different construction and must price its own positive diagonal, Fourier mass, and admissibility.

## 6. Prior art and novelty boundary

The Fejér/van-der-Corput shift weights are classical. Edeko, Kreidler and Nagel, *A dynamical proof of the van der Corput inequality* (Dynamical Systems 37 (2022), arXiv:2106.11835), provide a modern general reference for van der Corput inequalities. Irving, *Estimates for character sums and Dirichlet L-functions to smooth moduli* (IMRN 2016, arXiv:1503.07156), is a standard q-analogue van-der-Corput reference for character sums to smooth moduli. Modern well-factorable applications, including Maynard's large-modulus work (Memoirs AMS 306 (2025), arXiv:2006.07088), confirm the surrounding analytic setting but do not supply a theorem transfer to the staged Möbius kernel.

A targeted literature search on 22 September 2026 found the classical Fejér/vdC, q-vdC, and well-factorable frameworks, but no reason to treat `(3)`, `(5)`, or `(7)` as a separately named theorem. No novelty is claimed for their elementary gcd/counting content.

The durable Mathia contribution is the branch-specific consequence of applying those elementary identities to the exact `MC-463`--`MC-465` support gate: the apparent large-`g` advantage in the normalized compatible-shift ratio disappears when favorable mass is measured back in the original Fejér shift envelope, and this cancellation survives **arbitrary shift-independent outer coefficient weights**.

## Boundaries and falsification tests

- **This is a mass envelope, not an oscillatory estimate.** It controls how much standard Fejér shift/coefficient mass can enter favorable support cells, not the size of the translated-character sum on those cells.
- **Pair-dependent `M` remains load-bearing.** A concentration of coefficients on cells where the interval geometry makes `M_{r,r'}` large is not ruled out; equation `(8)` is the correct variable-threshold form.
- **Small `r'` remains an escape.** A dyadic application must use the actual lower scale `R` of the second outer factor.
- **Shift independence is load-bearing.** The outer coefficient pair mass must be fixed before the Fejér shift is chosen. This is true for the standard staged well-factorable component, but not for an intentionally shift-adaptive architecture.
- **The comparison denominator is the unrestricted original-shift Fejér envelope.** The compatible-mass ratio can still be large when `g` is large. The point is that the compatible supply is then proportionally small.
- **No arbitrary positive-kernel theorem is claimed.** `MC-416`--`MC-417` constrain redesigned positive finite-band filters, but `(7)` is proved only for the standard Fejér weights.
- **One-sided staging is asymmetric.** Reversing the staged expansion interchanges the roles of `r` and `r'`; no simultaneous two-sided quotient improvement is asserted.
- **No source-depth or RH information is imported.** The proof uses finite gcd arithmetic and the already-derived Fejér count only.

## Consequence for the research line

The first half of the outer-coefficient question left by `MC-465` is now substantially narrower. For the standard Fejér/q-vdC architecture, outer coefficients cannot beat the favorable-gcd sparsity merely by concentrating on pairs with large `(r,r')`: once one returns to the original shift variable, the gain in normalized quotient is exactly offset by the thinner compatible-shift supply, and the absolute favorable coefficient mass is controlled on the `M^2/r'` scale.

The live coefficient question is therefore no longer generic concentration on large outer gcd. It is concentration on cells where **the actual pair-dependent threshold `M_{r,r'}` is itself large relative to `sqrt(r')`**, or on small `r'`, together with enough aggregated `\widetilde\beta` participation and aligned residual-amplitude structure to retain a conductor-power gain. That is the next quantity that must be priced before attacking the full oscillatory family.