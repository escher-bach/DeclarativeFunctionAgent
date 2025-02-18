from .common import json
from typing import Dict, Any
import textwrap

def format_legal_analysis(analysis_results: Dict[str, Any], output_file: str) -> None:
    """
    Creates a nicely formatted text file from legal analysis results.
    
    Args:
        analysis_results: Dictionary containing analysis results for each document
        output_file: Path to save the formatted output
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for doc_name, analysis in analysis_results.items():
            # Document Header
            f.write("=" * 80 + "\n")
            f.write(f"Document Analysis: {doc_name}\n")
            f.write("=" * 80 + "\n\n")

            # Parsed Structure
            if 'parsed_structure' in analysis:
                f.write("📄 Document Structure\n")
                f.write("-" * 40 + "\n")
                
                # Metadata
                f.write("📋 Metadata:\n")
                for key, value in analysis['parsed_structure']['metadata'].items():
                    f.write(f"   • {key}: {value}\n")
                f.write("\n")
                
                # Sections
                f.write("📑 Sections:\n")
                for section, content in analysis['parsed_structure']['sections'].items():
                    f.write(f"   ▪ {section}:\n")
                    wrapped_content = textwrap.fill(content, width=70, initial_indent="     ", subsequent_indent="     ")
                    f.write(f"{wrapped_content}\n\n")
                
                # Clauses
                f.write("📎 Clauses:\n")
                for clause, content in analysis['parsed_structure']['clauses'].items():
                    f.write(f"   ▪ {clause}:\n")
                    wrapped_content = textwrap.fill(content, width=70, initial_indent="     ", subsequent_indent="     ")
                    f.write(f"{wrapped_content}\n\n")

            # Entities
            if 'entities' in analysis and not isinstance(analysis['entities'], dict) or \
               not analysis['entities'].get('error'):
                f.write("👥 Extracted Entities\n")
                f.write("-" * 40 + "\n")
                entities = analysis['entities'].get('entities', {})
                for entity_type, items in entities.items():
                    f.write(f"   • {entity_type.title()}:\n")
                    for item in items:
                        f.write(f"     - {item}\n")
                f.write("\n")

            # Key Facts
            if 'key_facts' in analysis and not isinstance(analysis['key_facts'], dict) or \
               not analysis['key_facts'].get('error'):
                f.write("🔑 Key Facts\n")
                f.write("-" * 40 + "\n")
                facts = analysis['key_facts'].get('key_facts', {})
                for fact_type, items in facts.items():
                    f.write(f"   • {fact_type.title()}:\n")
                    for item in items:
                        wrapped_item = textwrap.fill(item, width=70, initial_indent="     - ", subsequent_indent="       ")
                        f.write(f"{wrapped_item}\n")
                f.write("\n")

            # Legal Claims
            if 'legal_claims' in analysis and not isinstance(analysis['legal_claims'], dict) or \
               not analysis['legal_claims'].get('error'):
                f.write("⚖️ Legal Claims\n")
                f.write("-" * 40 + "\n")
                claims = analysis['legal_claims']
                if isinstance(claims, list):
                    for claim in claims:
                        f.write(f"   • Claim: {claim.get('claim', 'N/A')}\n")
                        f.write(f"     Basis: {claim.get('basis', 'N/A')}\n")
                        f.write(f"     Strength: {claim.get('strength', 'N/A')}\n")
                        f.write("     Related Clauses:\n")
                        for clause in claim.get('related_clauses', []):
                            f.write(f"       - {clause}\n")
                        f.write("\n")

            # Analysis
            if 'analysis' in analysis and not isinstance(analysis['analysis'], dict) or \
               not analysis['analysis'].get('error'):
                f.write("🔍 Legal Analysis\n")
                f.write("-" * 40 + "\n")
                analysis_data = analysis['analysis']
                if isinstance(analysis_data, dict):
                    # Key Arguments
                    if 'key_arguments' in analysis_data:
                        f.write("   • Key Arguments:\n")
                        for arg in analysis_data['key_arguments']:
                            wrapped_arg = textwrap.fill(arg, width=70, initial_indent="     - ", subsequent_indent="       ")
                            f.write(f"{wrapped_arg}\n")
                    
                    # Legal Basis
                    if 'legal_basis' in analysis_data:
                        f.write("\n   • Legal Basis:\n")
                        wrapped_basis = textwrap.fill(analysis_data['legal_basis'], width=70, 
                                                    initial_indent="     ", subsequent_indent="     ")
                        f.write(f"{wrapped_basis}\n")
                    
                    # Potential Issues
                    if 'potential_issues' in analysis_data:
                        f.write("\n   • Potential Issues:\n")
                        for issue in analysis_data['potential_issues']:
                            wrapped_issue = textwrap.fill(issue, width=70, initial_indent="     - ", 
                                                        subsequent_indent="       ")
                            f.write(f"{wrapped_issue}\n")
                    
                    # Recommendations
                    if 'recommendations' in analysis_data:
                        f.write("\n   • Recommendations:\n")
                        for rec in analysis_data['recommendations']:
                            wrapped_rec = textwrap.fill(rec, width=70, initial_indent="     - ", 
                                                      subsequent_indent="       ")
                            f.write(f"{wrapped_rec}\n")
                f.write("\n")

            # Summary
            if 'summary' in analysis and not isinstance(analysis['summary'], dict) or \
               not analysis['summary'].get('error'):
                f.write("📝 Document Summary\n")
                f.write("-" * 40 + "\n")
                summary = analysis['summary']
                if isinstance(summary, dict):
                    # Brief
                    if 'brief' in summary:
                        f.write("   • Brief Overview:\n")
                        wrapped_brief = textwrap.fill(summary['brief'], width=70, initial_indent="     ", 
                                                    subsequent_indent="     ")
                        f.write(f"{wrapped_brief}\n\n")
                    
                    # Key Points
                    if 'key_points' in summary:
                        f.write("   • Key Points:\n")
                        for point in summary['key_points']:
                            wrapped_point = textwrap.fill(point, width=70, initial_indent="     - ", 
                                                        subsequent_indent="       ")
                            f.write(f"{wrapped_point}\n")
                        f.write("\n")
                    
                    # Obligations
                    if 'obligations' in summary:
                        f.write("   • Obligations:\n")
                        for party, obligations in summary['obligations'].items():
                            f.write(f"     {party}:\n")
                            for obligation in obligations:
                                wrapped_obligation = textwrap.fill(obligation, width=70, 
                                                                initial_indent="       - ", 
                                                                subsequent_indent="         ")
                                f.write(f"{wrapped_obligation}\n")
                        f.write("\n")
                    
                    # Risk Assessment
                    if 'risk_assessment' in summary:
                        f.write("   • Risk Assessment:\n")
                        wrapped_risk = textwrap.fill(summary['risk_assessment'], width=70, 
                                                   initial_indent="     ", subsequent_indent="     ")
                        f.write(f"{wrapped_risk}\n")

            f.write("\n" + "=" * 80 + "\n\n")