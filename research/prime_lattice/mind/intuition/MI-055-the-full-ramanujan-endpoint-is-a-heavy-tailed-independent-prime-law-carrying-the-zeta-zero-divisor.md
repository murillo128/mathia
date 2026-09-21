# MI-055 — The full Ramanujan endpoint is a heavy-tailed independent-prime law carrying the zeta-zero divisor

**Evidence level:** exact structural synthesis from [PL-411](../../findings/PL-411-ramanujan-endpoint-bernoulli-law.md), with the Mellin factorization calibrated against the classical singular-series Dirichlet series.

The moving endpoint `q asymp H` left by PL-410 can be reorganized without truncating Ramanujan denominators. After the exact divisor Möbius transform is summed over all denominators, every odd divisor channel cancels and the surviving even channels define a probability law on odd square-free integers:

`nu(m)=C_2 prod_(p|m) 1/[p(p-2)]`,

with `sum_m nu(m)=1`. Equivalently, if `M=prod_(p>2) p^(X_p)`, then the prime coordinates are independent Bernoulli variables with

`P(X_p=1)=1/(p-1)^2`.

The complete cubic model statistic is exactly an expectation over this fixed law,

`2 A_eta^[2](H)=E[P_eta(H/(2M))]`.

Thus the true endpoint is not an uncontrolled union of moving square-free denominators. It is one canonical prime-coordinate probability space sampled through the archimedean Poisson kernel.

The law is heavy-tailed at precisely the scale where finite cusp-jet renormalization stops being integrable. PL-411 proves

`P(M>X) ~ 1/(2X)`

and

`E(M^a)<infinity iff a<1`.

So the first cubic cusp moment, and every higher cusp moment used by the finite interior expansion, diverges globally. This explains structurally why the exact finite counterterms of PL-410 can remove every fixed fractional interior yet cannot simply be summed termwise through the true endpoint.

Its Mellin transform `N(s)=E(M^(-s))` also factors exactly through the classical singular-series continuation. In particular it contains the divisor `1/zeta(2s+4)`, placing possible nontrivial-zero singularities at `s=rho/2-2`, on `Re s=-7/4` under RH. This recovers the zero-sensitive exponent from PL-404 inside a positive prime-lattice law rather than a moving denominator cutoff.

The endpoint question is therefore more concrete. One can now analyze the signed archimedean expectation against `nu`, or compare the actual prime source directly with this fixed probability carrier, instead of extending finite cusp jets toward `q/H=1`. Any RH criterion from the Mellin representation must still prove that the relevant zero poles are not canceled by numerator or local factors.

**Boundary.** PL-411 does not prove such noncancellation and therefore does not by itself give a new RH criterion. The Bernoulli law belongs to the model singular-series source, not the actual prime spectral measure. Its positivity and independence do not solve the source-replacement problem; they reorganize the exact model endpoint on which that comparison must be made.