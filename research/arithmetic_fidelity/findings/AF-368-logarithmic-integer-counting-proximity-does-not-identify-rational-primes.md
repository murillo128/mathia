# AF-368 — logarithmic integer-counting proximity does not identify rational primes

**Status:** `LITERATURE+DERIVED`, `DECISIVE-NEGATIVE`, `ARITHMETIC-FIDELITY`, `MATCHED-CONTROL`, `SOURCE-CLASS`, `BEURLING-BOUNDARY`, `NO-NOVELTY-CLAIM`

## Claim

Let `P` be the ordinary rational-prime system, so its generalized-integer counting function is exactly

\[
N_P(x)=\lfloor x\rfloor.
\]

A theorem of Rikard Olofsson gives the following sharp source-side obstruction: for **every** constant `c>0` there exists a Beurling prime system `Q\ne P` whose generalized-integer counting function satisfies

\[
\boxed{
|N_Q(x)-\lfloor x\rfloor|<c\log x.
}
\tag{1}
\]

Thus arbitrarily tight logarithmic scalar counting control does not identify the rational-prime system inside the Beurling category.

For fixed `c>0`, let

\[
\mathcal C_c
:=
\left\{
R:\ |N_R(x)-\lfloor x\rfloor|<c\log x
\text{ on the range of the stated bound}
\right\}
\tag{2}
\]

and let

\[
D_{\rm rat}(R)=\mathbf 1_{\{R=P\}}
\tag{3}
\]

be the exact rational-prime discriminator. The ordinary system belongs to every `\mathcal C_c` with zero counting error, while Olofsson supplies a nonordinary `Q\in\mathcal C_c`. Hence `D_rat` is nonconstant on every such retained regularity class:

\[
\boxed{
\text{no positive fixed multiple of }\log x
\text{ as a scalar integer-counting envelope forces }R=P.
}
\tag{4}
\]

This materially sharpens the source-class boundary left by AF-367. AF-367 shows that an arbitrarily long exact ordinary prime/integer prefix plus positive Euler-product structure and the much looser global class

\[
N_R(x)=x+O\!\left(x^{1/2}e^{c(\log x)^{2/3}}\right)
\]

still fails to determine Beurling-RH zero geometry. AF-368 moves the **global counting regularity** vastly closer to the ordinary integers—down to an arbitrarily small constant times `log x`—and still cannot recover even the underlying rational-prime identity.

The discriminators are different and must not be conflated: AF-368 does **not** prove that Olofsson's matched system has different RH status or different zero geometry. It proves a stronger statement only about source identity/provenance: extremely accurate scalar knowledge of `N(x)` remains compatible with a genuinely nonordinary prime system.

## Derivation

### 1. Olofsson's theorem gives a matched nonordinary source at every logarithmic tolerance

Olofsson studies Beurling's question of how closely a nonordinary generalized-prime system can imitate the ordinary integer-counting function. His theorem states that for every `c>0` there is a Beurling prime number system `Q\ne P` satisfying `(1)`. The same paper conjectures that logarithmic size is the optimal order of approximation.

The ordinary system `P` has zero discrepancy from `\lfloor x\rfloor`. Therefore any source description that retains only membership in the envelope class `(2)` identifies neither the generator system nor the exact rational-prime provenance: both `P` and at least one `Q\ne P` survive the same retained condition.

This is an exact fiber obstruction at the level of the declared retained datum. It is not a conditioning statement and does not depend on finite precision. The retained class itself contains incompatible values of `D_rat`.

### 2. Arbitrarily small constants do not repair the scalar counting gate

The quantifier `for every c>0` is the decisive strength. There is no fixed positive threshold constant `c_*` such that

\[
|N_R(x)-\lfloor x\rfloor|<c_*\log x
\]

would isolate the ordinary prime system among Beurling prime systems. Given any proposed `c_*>0`, Olofsson's theorem supplies a nonordinary control inside that same envelope.

Consequently, improving AF-367 merely by replacing its near-square-root counting remainder with `O(log x)` cannot make the retained **scalar counting class** rational-prime faithful. A successful source gate has to use additional structure or a genuinely stronger regime than every positive fixed logarithmic envelope.

Olofsson conjectures that the logarithmic order is best possible. That conjecture marks a natural open boundary for scalar counting alone, but it is not used as evidence here: AF-368 claims only the proved non-rigidity at every positive multiple of `log x`.

### 3. Exact support is qualitatively stronger than counting proximity

Jeffrey Lagarias' Delone classification clarifies what type of information `(1)` still omits. If a Beurling generalized-integer set has the Delone property and is actually contained in the positive integers, Lagarias proves that it has unique factorization and that its generalized primes consist of all but finitely many ordinary primes together with finitely many composite integers.

This does not by itself force the exact ordinary prime system, but it shows a qualitative jump between two kinds of source information:

\[
\text{very small scalar counting discrepancy}
\quad\not\Rightarrow\quad
\text{ordinary arithmetic support},
\tag{5}
\]

whereas exact integer support plus Delone geometry collapses the allowed generalized-prime freedom to finite arithmetic modifications.

Thus the live source-side hierarchy is not well described by the magnitude of `N_R(x)-\lfloor x\rfloor` alone. Exact support, factorization structure, cancellation laws, functional relations, or other nonlocal arithmetic constraints carry information that a scalar count can miss even when that count is logarithmically close to the classical one.

### 4. Relation to the current finite-horizon boundary

AF-366 and AF-367 expose completion freedom after finite observations. AF-368 is different: its obstruction is global in `x`. The retained information can constrain the generalized-integer count at every scale to lie inside an arbitrarily narrow logarithmic tube around the ordinary count, yet the generator system need not be `P`.

Accordingly, simply replacing

\[
\text{finite exact prefix}
\]

by

\[
\text{global scalar density/counting accuracy}
\]

is not enough to recover rational-prime provenance. The source gate must preserve a structural property not encoded by that scalar tube.

This narrows the current research question in `mind/RESEARCH_LINES.md`: among the candidate ordinary-arithmetic completion laws, **exact support or genuinely arithmetic cancellation/functional structure is qualitatively more promising than progressively tighter scalar bounds on `N(x)`** unless one crosses the still-open sublogarithmic rigidity boundary.

## Prior art and novelty assessment

No novelty is claimed for the Beurling construction or for the Delone classification.

The primary source for the logarithmic approximation theorem is:

- Rikard Olofsson, **“Properties of the Beurling generalized primes,”** *Journal of Number Theory* **131** (2011), 45–58, DOI `10.1016/j.jnt.2010.06.014`. The paper proves that for every `c>0` there is a Beurling prime system `Q\ne P` with `|N_Q(x)-\lfloor x\rfloor|<c\log x` and conjectures that logarithmic order is best possible.

The structural boundary for integer-supported Delone systems is:

- Jeffrey C. Lagarias, **“Beurling generalized integers with the Delone Property,”** *Forum Mathematicum* **11** (1999), 295–312, DOI `10.1515/FORM.1999.295`. Lagarias proves unique factorization for Delone generalized-integer sets and classifies those contained in the positive integers; their generalized-prime sets consist of all but finitely many ordinary primes plus finitely many composites.

The Arithmetic Fidelity content is the source-information comparison. Olofsson's theorem is an exact matched-control obstruction showing that even `c\log x` scalar counting fidelity, with arbitrarily small positive `c`, does not preserve rational-prime identity. Lagarias then identifies an adjacent stronger information layer—exact arithmetic support plus Delone structure—where the source ambiguity collapses from unrestricted Beurling freedom to finite modifications. This sharpens the current search for an ordinary-arithmetic completion law without claiming a new theorem in generalized-prime theory.

## Boundaries and failure modes

- Equation `(1)` is a statement about a **counting-error envelope**, not equality of the complete counting functions. A mechanism retaining the exact step function `N_R(x)` has strictly more information and is not refuted here.
- The finding distinguishes `Q\ne P`; it does not assert that Olofsson's `Q` has a prescribed zero divisor, violates Beurling RH, or differs from `zeta(s)` in any particular zero region. Those would require separate theorems.
- The logarithmic envelope does not encode the exact generalized-integer support, multiplicities, generalized von Mangoldt weights, Möbius data, functional equation, or arithmetic-progression structure.
- Lagarias' theorem does not say that every integer-supported Delone Beurling system equals the ordinary one. Finite prime/composite modifications remain possible.
- Olofsson's optimality statement at logarithmic order is a conjecture. No rigidity theorem at `o(log x)` is claimed here.
- A source condition stronger than scalar counting may still fail for another reason. AF-368 only removes one tempting repair: progressively tightening `N(x)` to a fixed positive logarithmic envelope.

## Decisive audit test

Any proposed source-side repair of AF-367 that claims rational-prime specificity from generalized-integer counting regularity alone should first be tested against Olofsson's family.

If the retained source condition is implied by

\[
|N_R(x)-\lfloor x\rfloor|<c\log x
\]

for some fixed `c>0`, and it does not inspect additional support/factorization/cancellation/functional data, then the condition cannot identify `P` in the Beurling category.

To escape this obstruction, the proposal must use a genuinely stronger retained property and show why Olofsson's nonordinary controls cannot satisfy it. Exact support, a sublogarithmic rigidity theorem, an ordinary-arithmetic cancellation law, or a rigid analytic/functional coupling are legitimate candidate escape routes; none is established by AF-368 itself.
