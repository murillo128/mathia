# MI-048 — Finite Wang cross-order interactions are confluent exponential polynomials

**Evidence level:** exact structural synthesis from [VIS-349](../../findings/VIS-349-wang-cross-order-confluent-exponential-polynomial.md), extending VIS-348 without assuming exact cancellation of lower Wang moments. The confluent exponential-polynomial/ODE structure is classical; the line-specific content is its exact realization by Wang's finite tail hierarchy.

For the first `q` Wang tail orders, keep all moment polynomials simultaneously and form

`E_(q,X)(xi)=sum_(k=1)^q beta_k xi^(q-k) P_(k,X)(xi)`.

Grouping by translation phase gives

`E_(q,X)(xi)=sum_b exp(-i b xi) Q_(b,q,X)(xi)`,

where each `Q_b` is a polynomial of degree at most `q-1`. Equivalently, `E_q` lies in the finite confluent exponential space spanned by `xi^r exp(-i b xi)` and is annihilated by `prod_b(D+i b)^q`.

This closes the exact algebraic version of the cross-order escape. If `E_q` vanishes on any nonempty interval, analyticity and linear independence force every phase-fiber moment `S_(b,k,X)` to vanish for `k<=q`; exact cancellation between several nonzero inverse-frequency orders creates no new nullspace beyond the ordinary order-by-order moment equations.

Approximate local cancellation is also reduced to the same finite-dimensional object. If the bank gains one extra order on `J_X subset [X,2X]`, then

`sup_(J_X)|E_(q,X)| <= [2^q C_0 + C_q T_(q+1,X)]/X`.

Thus **finite cross-order interaction is not a new functional category; it is a concentration problem for a confluent exponential polynomial with explicit phase multiplicities and coefficient conditioning**. VIS-348 is the special case where lower moments vanish and the first surviving coefficient reduces to an ordinary exponential polynomial.

**Boundary.** VIS-349 does not yet provide a sharp Turán--Nazarov-style estimate uniform under moving/coalescing phases and polynomial coefficients. Approximate concentration may still be paid for by dimension growth, phase collisions, shrinking windows or ill-conditioning. Frequency/source-dependent coefficients, infinite expansions and direct signed cancellation in the theta remainder remain outside the finite-bank reduction.