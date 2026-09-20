# PL-389 — Zeta universality ejects the vertical symbol from the almost-periodic index algebra before the critical line

**Evidence:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + DECISIVE-NEGATIVE`.

**Parent finding:** `PL-388`.

**Related findings:** `PL-005`, `PL-011`, `PL-387`, `PL-388`.

**Status:** `THE-STANDARD-COBURN--DOUGLAS-ALMOST-PERIODIC/WIENER--HOPF-INDEX-OF-PL-388-CANNOT-BE-CONTINUED-AS-A-NATIVE-ZETA-SYMBOL-INDEX-INTO-THE-OPEN-CRITICAL-STRIP. FOR-EVERY-FIXED-1/2<sigma<1, VERTICAL-VALUE-DISTRIBUTION-MAKES-t-MAPS-TO-zeta(sigma+it)-DENSE-IN-C, HENCE-UNBOUNDED-AND-ARBITRARILY-CLOSE-TO-ZERO. THEREFORE-THE-VERTICAL-ZETA-SYMBOL-IS-NOT-IN-THE-BOHR-UNIFORM-AP-ALGEBRA; EVEN-UNDER-RH, WHEN-THE-LINE-IS-ZERO-FREE, ITS-INVERSE-IS-UNBOUNDED-AND-SO-IT-IS-NOT-AP-INVERTIBLE. AT-sigma>1-THE-EULER-PRODUCT-SYMBOL-IS-AP-INVERTIBLE-WITH-ZERO-MEAN-MOTION-INDEX, WHILE-AT-sigma=1-THE-POLE-ALREADY-PREVENTS-A-GLOBAL-BOUNDED-SYMBOL. THUS-THE-NATIVE-AP-INDEX-EXITS-ITS-ALGEBRA-AT-THE-PNT-BOUNDARY, NOT-AT-Re(s)=1/2. ANY-SURVIVING-INDEX-PROGRAM-MUST-CHANGE-THE-SYMBOL-CLASS-OR-ADD-TARGET-RELATIVE/RENORMALIZED-STRUCTURE`.

## Claim

For a fixed real number

\[
\frac12<\sigma<1,
\]

write

\[
Z_\sigma(t)=\zeta(\sigma+it),\qquad t\in\mathbb R.
\tag{PL389-1}
\]

Then

\[
\boxed{\overline{Z_\sigma(\mathbb R)}=\mathbb C.}
\tag{PL389-2}
\]

Consequently

\[
\boxed{\sup_{t\in\mathbb R}|Z_\sigma(t)|=\infty,
\qquad
\inf_{t\in\mathbb R}|Z_\sigma(t)|=0.}
\tag{PL389-3}
\]

Since every Bohr uniformly almost-periodic function is bounded,

\[
\boxed{Z_\sigma\notin AP(\mathbb R)
\qquad\left(\frac12<\sigma<1\right).}
\tag{PL389-4}
\]

Moreover, even under RH, when `zeta(sigma+it)` has no zeros for such `sigma`, (PL389-3) implies

\[
\sup_t\frac1{|\zeta(\sigma+it)|}=\infty,
\tag{PL389-5}
\]

so the zero-free vertical symbol is still not invertible in `AP(R)`.

This sharply closes the standard almost-periodic index route left open by `PL-388`. For `sigma>1`, the absolutely convergent Euler product gives an invertible `AP(R)` symbol with zero mean-motion/Fredholm index. That symbol does **not** remain inside the same bounded almost-periodic algebra when analytically continued across `Re(s)=1`; the obstruction occurs before the critical line and persists even if RH is assumed.

## 1. Fixed-line value distribution forces unboundedness and approach to zero

The load-bearing theorem is classical zeta value distribution. An audit-friendly modern source already catalogued in `research/prime_lattice/SOURCES.md` is Łukasz Pańkowski, “Joint Value-Distribution of Shifts of the Riemann Zeta-Function,” *Results in Mathematics* **77** (2022), Article 76, DOI `10.1007/s00025-022-01609-4`.

Pańkowski proves that for a fixed complex number `s` in the right open half of the critical strip and distinct positive rational numbers `d_1,...,d_n`, arbitrary prescribed complex values can be approximated by

\[
\zeta(s+i d_1\tau),\ldots,\zeta(s+i d_n\tau)
\]

for infinitely many real `tau`. Taking `n=1`, `d_1=1`, and `s=\sigma+i t_0` gives, for every `w in C` and every `epsilon>0`, infinitely many `tau` with

\[
|\zeta(\sigma+i(t_0+\tau))-w|<\varepsilon.
\tag{PL389-6}
\]

Since translating `t` by the fixed `t_0` does not change the value set, (PL389-2) follows.

Now choose targets with arbitrarily large modulus in (PL389-6) to obtain the first statement in (PL389-3), and choose `w=0` with `epsilon -> 0` to obtain the second. No Euler product is used here. This is genuine critical-strip analytic-continuation/value-distribution input, not a formal continuation of the prime expansion valid at `sigma>1`.

The same conclusion is classically associated with Bohr--Courant denseness and is strengthened in various forms by Voronin universality. No novelty is claimed for the denseness theorem itself.

## 2. Why zero-freeness under RH does not restore almost-periodic invertibility

The Coburn--Douglas symbol algebra used in `PL-387`--`PL-388` is the `C*`-algebra `AP(R)` of **uniformly** almost-periodic functions. In particular,

\[
AP(\mathbb R)\subset C_b(\mathbb R).
\tag{PL389-7}
\]

Equation (PL389-3) therefore immediately gives (PL389-4).

There is a second obstruction that matters for an index interpretation. In a unital commutative `C*`-algebra of bounded functions, an element represented by a nowhere-zero function is invertible only when its reciprocal lies in the algebra; in particular it must be bounded away from zero. Thus pointwise zero-freeness is weaker than `AP` invertibility.

Assume RH and fix `1/2<sigma<1`. Then `zeta(sigma+it)` is nowhere zero on that vertical line. Nevertheless (PL389-3) gives sequences `t_j` with

\[
|\zeta(\sigma+i t_j)|\longrightarrow0,
\]

and hence

\[
|1/\zeta(\sigma+i t_j)|\longrightarrow\infty.
\]

Therefore RH does not move `Z_sigma` into `AP(R)^times`; it only changes the reason invertibility fails from possible actual zeros to arbitrarily close returns to zero plus unbounded range.

This distinction is important for the research line. An almost-periodic Fredholm index cannot detect RH merely by asking whether the analytically continued vertical zeta function is zero-free: the relevant bounded-symbol invertibility condition already fails unconditionally throughout the entire open strip `1/2<sigma<1`.

## 3. The index path exits at `Re(s)=1`, not at the critical line

`PL-388` established that for every fixed `sigma>1`,

\[
\log\zeta(\sigma+it)
=
\sum_p\sum_{k\ge1}
\frac{p^{-k\sigma}}{k}e^{-itk\log p}
\tag{PL389-8}
\]

converges absolutely and uniformly in `t`. Hence

\[
Z_\sigma(t)=\exp(\log\zeta(\sigma+it))
\]

is an invertible element of `AP(R)` in the identity component, and its Coburn--Douglas--Schaeffer--Singer mean-motion index is zero.

At `sigma=1`, the global vertical function contains the pole `zeta(1)` at `t=0`, so it is already not a bounded continuous symbol on `R`. For every `1/2<sigma<1`, Section 1 gives the stronger universality obstruction (PL389-4). Thus the natural family of standard bounded symbols has the sharp qualitative pattern

\[
\sigma>1:\quad Z_\sigma\in AP(\mathbb R)^\times,
\qquad
\frac12<\sigma\le1:\quad Z_\sigma\notin AP(\mathbb R)
\tag{PL389-9}
\]

where the `sigma=1` statement is due to the pole and the open-strip statement to value distribution.

Accordingly there is no continuous path of **native zeta symbols inside the classical `AP` invertible group** that starts in the Euler-product half-plane and reaches the critical strip. The standard index cannot acquire RH-sensitive jumps at off-critical zeros because the family leaves its symbol algebra before those zeros become the relevant issue.

This is stronger than the zero-index observation of `PL-388`: the problem is not merely that the index happens to vanish where the Euler product converges. The classical bounded almost-periodic index is not even defined on the analytically continued zeta vertical symbol in the open critical strip.

## 4. Adversarial controls and boundaries

The conclusion is deliberately restricted to the **standard bounded Bohr almost-periodic/Wiener--Hopf symbol algebra** of Coburn--Douglas and to the native vertical symbol `t -> zeta(sigma+it)`. It does not rule out unbounded or affiliated Wiener--Hopf operators, Besicovitch/Stepanov almost-periodic classes, weighted symbols, local or finite-window argument-principle indices, nonlinear renormalizations, or target-relative compressions such as the Nyman/Weil structures already isolated elsewhere in the line.

Nor does (PL389-4) say that prime-frequency dynamics disappear in the strip. The value-distribution theorem itself is built from the arithmetic/analytic structure of zeta. The negative result is narrower: that structure is too wild to remain in the bounded `AP` `C*`-algebra whose index recovered the additive prime-lattice energy in `PL-388`.

The RH stress test is decisive for this route. If the only obstruction had been actual off-critical zeros, one could hope that RH made the vertical symbol invertible and turned the index into a localization criterion. Equation (PL389-5) falsifies that hope: even in the RH world, universality drives the symbol arbitrarily close to zero and arbitrarily far in modulus.

A future extension should therefore be audited against the following failure mode: if it enlarges the symbol class enough to contain `Z_sigma` for `1/2<sigma<1`, it must still provide a Fredholm/invertibility notion whose rigidity is **not** destroyed by the dense value distribution (PL389-2). Merely replacing uniform `AP` by a larger function class does not by itself create an RH mechanism.

## 5. Prior-art and novelty audit

The fixed-line value-distribution input is prior art. The modern theorem used here is Pańkowski (2022), already source 9 in the line bibliography. Classical Bohr--Courant denseness and Voronin universality are stronger historical/background routes to the same unboundedness/near-zero conclusion.

The boundedness of Bohr uniformly almost-periodic functions and the invertibility criterion in a uniform `C*`-algebra are standard functional analysis. The Coburn--Douglas almost-periodic quotient and real-valued mean-motion index were already audited in `PL-387`--`PL-388`.

No novelty is claimed for any of these ingredients. The durable Mathia delta is the **route-specific incompatibility** obtained by composing them: the exact standard symbol algebra whose index canonically reads `log n` cannot carry the analytically continued zeta vertical symbol across `Re(s)=1`, and RH would not repair this failure. A targeted audit found the ingredients to be classical; the present result is recorded as a decisive negative boundary for this prime-lattice index route rather than as a new zeta theorem.

## Consequence for the research line

The ambient half-line translation index program is now classified one step further. `PL-388` showed that the natural index exactly recovers the prime-lattice energy `log n` but is zero on the Euler-product zeta symbol for `sigma>1`. The present result shows that trying to carry that same bounded almost-periodic index into the critical strip fails structurally, not just computationally.

Therefore a continuation-sensitive index route must introduce genuinely new structure: an unbounded/renormalized symbol theory with a nontrivial Fredholm notion, or an arithmetic target/compression that survives dense vertical value distribution. Reusing the standard `AP(R)` Wiener--Hopf index cannot make `Re(s)=1/2` a distinguished spectral boundary.